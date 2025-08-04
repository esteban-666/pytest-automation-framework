"""
Pytest configuration and fixtures for the automation framework.
"""

import logging
import os
import sys
from pathlib import Path
from typing import Any, Dict, Generator
from unittest.mock import Mock

import pytest

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from utils.api_client import APIClient

# Import framework modules
from utils.config_manager import ConfigManager
from utils.logger import setup_logger
from utils.webdriver_manager import WebDriverManager

# Setup logging
logger = setup_logger()

# Load configuration
config = ConfigManager()


@pytest.fixture(scope="session")
def test_config() -> Dict[str, Any]:
    """Provide test configuration for the entire test session."""
    return config.get_config()


@pytest.fixture(scope="session")
def api_base_url(test_config) -> str:
    """Provide API base URL for the test session."""
    return test_config.get("api", {}).get("base_url", "http://localhost:8000")


@pytest.fixture(scope="session")
def web_base_url(test_config) -> str:
    """Provide web base URL for the test session."""
    return test_config.get("web", {}).get("base_url", "http://localhost:3000")


@pytest.fixture(scope="function")
def driver(request) -> Generator:
    """Provide WebDriver instance for web tests."""
    import signal
    from selenium.common.exceptions import WebDriverException
    
    # Detect CI environment
    is_ci = os.getenv("CI") == "true" or os.getenv("GITHUB_ACTIONS") == "true"
    
    def timeout_handler(signum, frame):
        raise TimeoutError("WebDriver setup timed out")
    
    # Set different timeouts for CI vs local
    setup_timeout = 60 if is_ci else 30  # More time for CI setup
    page_load_timeout = 15 if is_ci else 30  # Even faster timeouts for CI to prevent hanging
    implicit_wait = 3 if is_ci else 10  # Very fast implicit waits for CI
    script_timeout = 10 if is_ci else 20  # Conservative script timeout for CI
    
    # Set a timeout for WebDriver setup
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(setup_timeout)
    
    try:
        print(f"🔧 Initializing WebDriver... (CI: {is_ci})")
        driver_manager = WebDriverManager()
        driver = driver_manager.get_driver()

        # Set implicit wait (shorter for CI)
        driver.implicitly_wait(implicit_wait)

        # Set window size
        driver.set_window_size(1920, 1080)
        
        # Set page load timeout (shorter for CI)
        driver.set_page_load_timeout(page_load_timeout)
        
        # Set script timeout (conservative for CI)
        driver.set_script_timeout(script_timeout)
        
        print("✅ WebDriver initialized successfully")
        signal.alarm(0)  # Cancel the alarm
        
        yield driver

    except (WebDriverException, TimeoutError) as e:
        signal.alarm(0)  # Cancel the alarm
        print(f"❌ WebDriver initialization failed: {e}")
        if is_ci:
            # In CI, try to provide more debugging info
            print("🔍 CI Environment Debug Info:")
            print(f"   - DISPLAY: {os.getenv('DISPLAY', 'Not set')}")
            print(f"   - CI: {os.getenv('CI', 'Not set')}")
            print(f"   - GITHUB_ACTIONS: {os.getenv('GITHUB_ACTIONS', 'Not set')}")
        raise
    except Exception as e:
        signal.alarm(0)  # Cancel the alarm
        print(f"❌ Unexpected error during WebDriver setup: {e}")
        raise
    finally:
        signal.alarm(0)  # Ensure alarm is cancelled
        try:
            if 'driver' in locals():
                print("🧹 Cleaning up WebDriver...")
                driver.quit()
                print("✅ WebDriver cleanup completed")
        except Exception as e:
            print(f"⚠️ Warning: WebDriver cleanup failed: {e}")


@pytest.fixture(scope="function")
def api_client(api_base_url) -> APIClient:
    """Provide API client for API tests."""
    return APIClient(base_url=api_base_url)


@pytest.fixture(scope="function")
def mock_api_response():
    """Provide mock API response for testing."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"status": "success", "data": {}}
    mock_response.text = '{"status": "success", "data": {}}'
    return mock_response


@pytest.fixture(scope="function")
def test_data():
    """Provide test data for parameterized tests."""
    return {
        "valid_user": {
            "username": "testuser",
            "email": "test@example.com",
            "password": "TestPassword123!",
        },
        "invalid_user": {"username": "", "email": "invalid-email", "password": "weak"},
        "admin_user": {
            "username": "admin",
            "email": "admin@example.com",
            "password": "AdminPassword123!",
        },
    }


@pytest.fixture(scope="function")
def cleanup_test_data():
    """Cleanup test data after tests."""
    yield
    # Add cleanup logic here
    logger.info("Cleaning up test data")


@pytest.fixture(scope="session")
def test_environment():
    """Provide test environment information."""
    return {
        "env": os.getenv("TEST_ENV", "staging"),
        "platform": os.getenv("PLATFORM", "desktop"),
        "browser": os.getenv("BROWSER", "chrome"),
        "headless": os.getenv("HEADLESS", "true").lower() == "true",
    }


@pytest.fixture(scope="function")
def wait_for_element(driver):
    """Provide explicit wait utility for web elements."""
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait

    def wait(element_locator, timeout=20, condition=EC.presence_of_element_located):
        return WebDriverWait(driver, timeout).until(condition(element_locator))

    return wait


@pytest.fixture(scope="function")
def take_screenshot(driver):
    """Provide screenshot utility."""

    def capture_screenshot(name):
        screenshot_path = f"reports/screenshots/{name}.png"
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        driver.save_screenshot(screenshot_path)
        logger.info(f"Screenshot saved: {screenshot_path}")
        return screenshot_path

    return capture_screenshot


@pytest.fixture(scope="function")
def generate_test_data():
    """Provide test data generation utility."""
    from faker import Faker

    fake = Faker()

    def generate_user_data():
        return {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "address": fake.address(),
            "company": fake.company(),
        }

    return generate_user_data


# Pytest hooks
def pytest_configure(config):
    """Configure pytest with custom markers and settings."""
    # Add custom markers
    config.addinivalue_line("markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')")
    config.addinivalue_line("markers", "critical: marks tests as critical")
    config.addinivalue_line("markers", "api: marks tests as API tests")
    config.addinivalue_line("markers", "ui: marks tests as UI tests")
    config.addinivalue_line("markers", "unit: marks tests as unit tests")
    
    # Set default timeout for all tests
    config.addinivalue_line("addopts", "--timeout=300")
    
    # Configure test collection to be more efficient
    config.addinivalue_line("addopts", "--tb=short")
    
    print("🔧 Pytest configured with custom markers and settings")


def pytest_runtest_setup(item):
    """Setup before each test."""
    logger.info(f"Starting test: {item.name}")


def pytest_runtest_teardown(item, nextitem):
    """Cleanup after each test."""
    logger.info(f"Completed test: {item.name}")


def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers and handle slow tests."""
    # Add markers based on test file location
    for item in items:
        # Use pathlib.Path for better compatibility
        test_path = str(item.path)
        
        if "test_api" in test_path:
            item.add_marker(pytest.mark.api)
        elif "test_ui" in test_path or "test_e2e" in test_path:
            item.add_marker(pytest.mark.ui)
        elif "test_unit" in test_path or "test_math" in test_path:
            item.add_marker(pytest.mark.unit)
        
        # Mark E2E tests as slow by default
        if "test_ui" in test_path or "test_e2e" in test_path:
            item.add_marker(pytest.mark.slow)
    
    print(f"📋 Collected {len(items)} tests with appropriate markers")


def pytest_html_report_title(report):
    """Customize HTML report title."""
    report.title = "Pytest Automation Framework - Test Report"


def pytest_html_results_summary(prefix, summary, postfix):
    """Customize HTML report summary."""
    prefix.extend(
        [
            "<h2>Test Environment</h2>",
            f"<p><strong>Environment:</strong> {os.getenv('TEST_ENV', 'staging')}</p>",
            f"<p><strong>Platform:</strong> {os.getenv('PLATFORM', 'desktop')}</p>",
            f"<p><strong>Browser:</strong> {os.getenv('BROWSER', 'chrome')}</p>",
        ]
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_path = f"reports/screenshots/{item.name}_failed.png"
            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
            driver.save_screenshot(screenshot_path)
            logger.info(f"Screenshot saved: {screenshot_path}")


# Create necessary directories
os.makedirs("reports", exist_ok=True)
os.makedirs("reports/screenshots", exist_ok=True)
os.makedirs("reports/coverage", exist_ok=True)
os.makedirs("data", exist_ok=True)
