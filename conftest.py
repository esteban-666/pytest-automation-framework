"""
Pytest configuration and fixtures for the automation framework.
"""
import os
import sys
import pytest
import logging
from pathlib import Path
from typing import Generator, Dict, Any
from unittest.mock import Mock

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Import framework modules
from utils.config_manager import ConfigManager
from utils.logger import setup_logger
from utils.webdriver_manager import WebDriverManager
from utils.api_client import APIClient

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
    driver_manager = WebDriverManager()
    driver = driver_manager.get_driver()
    
    # Set implicit wait
    driver.implicitly_wait(10)
    
    # Set window size
    driver.set_window_size(1920, 1080)
    
    yield driver
    
    # Cleanup
    driver.quit()


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
            "password": "TestPassword123!"
        },
        "invalid_user": {
            "username": "",
            "email": "invalid-email",
            "password": "weak"
        },
        "admin_user": {
            "username": "admin",
            "email": "admin@example.com",
            "password": "AdminPassword123!"
        }
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
        "headless": os.getenv("HEADLESS", "true").lower() == "true"
    }


@pytest.fixture(scope="function")
def wait_for_element(driver):
    """Provide explicit wait utility for web elements."""
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
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
            "company": fake.company()
        }
    
    return generate_user_data


# Pytest hooks
def pytest_configure(config):
    """Configure pytest with custom markers and metadata."""
    # Add custom markers
    config.addinivalue_line("markers", "smoke: marks tests as smoke tests")
    config.addinivalue_line("markers", "regression: marks tests as regression tests")
    config.addinivalue_line("markers", "e2e: marks tests as end-to-end tests")
    config.addinivalue_line("markers", "api: marks tests as API tests")
    config.addinivalue_line("markers", "unit: marks tests as unit tests")
    config.addinivalue_line("markers", "integration: marks tests as integration tests")
    config.addinivalue_line("markers", "slow: marks tests as slow running")
    config.addinivalue_line("markers", "flaky: marks tests as potentially flaky")
    config.addinivalue_line("markers", "critical: marks tests as critical functionality")
    config.addinivalue_line("markers", "performance: marks tests as performance tests")
    config.addinivalue_line("markers", "security: marks tests as security tests")
    config.addinivalue_line("markers", "mobile: marks tests as mobile tests")
    config.addinivalue_line("markers", "web: marks tests as web tests")
    config.addinivalue_line("markers", "database: marks tests as database tests")
    config.addinivalue_line("markers", "ui: marks tests as UI tests")
    config.addinivalue_line("markers", "accessibility: marks tests as accessibility tests")
    config.addinivalue_line("markers", "visual: marks tests as visual regression tests")
    config.addinivalue_line("markers", "data_driven: marks tests as data-driven tests")
    config.addinivalue_line("markers", "parallel: marks tests that can run in parallel")
    config.addinivalue_line("markers", "sequential: marks tests that must run sequentially")


def pytest_runtest_setup(item):
    """Setup before each test."""
    logger.info(f"Starting test: {item.name}")


def pytest_runtest_teardown(item, nextitem):
    """Cleanup after each test."""
    logger.info(f"Completed test: {item.name}")


def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers based on test location."""
    for item in items:
        # Add markers based on test file location
        if "unit" in str(item.fspath):
            item.add_marker(pytest.mark.unit)
        elif "integration" in str(item.fspath):
            item.add_marker(pytest.mark.integration)
        elif "e2e" in str(item.fspath):
            item.add_marker(pytest.mark.e2e)
        elif "api" in str(item.fspath):
            item.add_marker(pytest.mark.api)


def pytest_html_report_title(report):
    """Customize HTML report title."""
    report.title = "Pytest Automation Framework - Test Report"


def pytest_html_results_summary(prefix, summary, postfix):
    """Customize HTML report summary."""
    prefix.extend([
        "<h2>Test Environment</h2>",
        f"<p><strong>Environment:</strong> {os.getenv('TEST_ENV', 'staging')}</p>",
        f"<p><strong>Platform:</strong> {os.getenv('PLATFORM', 'desktop')}</p>",
        f"<p><strong>Browser:</strong> {os.getenv('BROWSER', 'chrome')}</p>",
    ])


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
