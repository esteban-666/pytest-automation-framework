"""
WebDriver manager for browser automation.
"""

import os
import time
from typing import Any, Dict, Optional

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.safari.service import Service as SafariService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

try:
    from playwright.sync_api import sync_playwright

    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False
from utils.config_manager import ConfigManager
from utils.logger import logger


class WebDriverManager:
    """Manages WebDriver instances for different browsers."""

    def __init__(self):
        self.config = ConfigManager()
        self.driver = None

    def get_driver(
        self, browser: str = None, headless: bool = None, **kwargs
    ) -> webdriver.Remote:
        """
        Get a WebDriver instance.

        Args:
            browser: Browser name (chrome, firefox, edge, safari)
            headless: Run in headless mode
            **kwargs: Additional browser options

        Returns:
            WebDriver instance
        """
        browser = browser or self.config.get("browser.name", "chrome")
        headless = (
            headless
            if headless is not None
            else self.config.get("browser.headless", True)
        )

        logger.info(f"Initializing {browser} WebDriver (headless: {headless})")

        if browser.lower() == "chrome":
            self.driver = self._get_chrome_driver(headless, **kwargs)
        elif browser.lower() == "firefox":
            self.driver = self._get_firefox_driver(headless, **kwargs)
        elif browser.lower() == "edge":
            self.driver = self._get_edge_driver(headless, **kwargs)
        elif browser.lower() == "safari":
            self.driver = self._get_safari_driver(**kwargs)
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        # Set timeouts
        implicit_wait = self.config.get("web.implicit_wait", 10)
        page_load_timeout = self.config.get("web.page_load_timeout", 30)

        self.driver.implicitly_wait(implicit_wait)
        self.driver.set_page_load_timeout(page_load_timeout)

        # Set window size
        window_size = self.config.get(
            "web.window_size", {"width": 1920, "height": 1080}
        )
        self.driver.set_window_size(window_size["width"], window_size["height"])

        logger.info(f"WebDriver initialized successfully: {browser}")
        return self.driver

    def _get_chrome_driver(self, headless: bool = True, **kwargs) -> webdriver.Chrome:
        """Get Chrome WebDriver instance."""
        options = ChromeOptions()

        # Detect CI environment
        is_ci = os.getenv("CI") == "true" or os.getenv("GITHUB_ACTIONS") == "true" or os.getenv("BROWSER_CI_MODE") == "true"
        
        # Override headless setting in CI
        if is_ci or os.getenv("BROWSER_HEADLESS") == "true":
            headless = True

        if headless:
            options.add_argument("--headless")

        # Essential Chrome options for stability
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-blink-features=AutomationControlled")
        
        # CI-specific optimizations
        if is_ci:
            logger.info("🚀 CI environment detected - applying CI-specific optimizations")
            # Performance optimizations for CI
            options.add_argument("--disable-background-timer-throttling")
            options.add_argument("--disable-backgrounding-occluded-windows")
            options.add_argument("--disable-renderer-backgrounding")
            options.add_argument("--disable-features=TranslateUI")
            options.add_argument("--disable-hang-monitor")
            options.add_argument("--disable-prompt-on-repost")
            options.add_argument("--disable-domain-reliability")
            options.add_argument("--disable-component-extensions-with-background-pages")
            options.add_argument("--disable-default-apps")
            options.add_argument("--disable-sync")
            options.add_argument("--disable-translate")
            options.add_argument("--disable-background-networking")
            options.add_argument("--disable-client-side-phishing-detection")
            options.add_argument("--disable-component-update")
            options.add_argument("--disable-ipc-flooding-protection")
            options.add_argument("--memory-pressure-off")
            options.add_argument("--max_old_space_size=4096")
            # Reduce resource usage in CI
            options.add_argument("--disable-plugins")
            options.add_argument("--disable-background-networking")
            options.add_argument("--disable-default-apps")
        else:
            # Check if performance optimizations are enabled for local environment
            enable_performance_optimizations = self.config.get("browser.performance_optimizations", False)
            if enable_performance_optimizations:
                logger.info("🚀 Performance optimizations enabled for Chrome")
                options.add_argument("--memory-pressure-off")
                options.add_argument("--disable-background-timer-throttling")
                options.add_argument("--disable-backgrounding-occluded-windows")
                options.add_argument("--disable-renderer-backgrounding")
            else:
                logger.info("⚡ Standard Chrome configuration")
        
        # Automation detection prevention
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        # User agent
        user_agent = self.config.get("browser.user_agent")
        if user_agent:
            options.add_argument(f"--user-agent={user_agent}")

        # Download path
        download_path = self.config.get("browser.download_path", "./downloads")
        os.makedirs(download_path, exist_ok=True)
        prefs = {
            "download.default_directory": os.path.abspath(download_path),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
        }
        options.add_experimental_option("prefs", prefs)

        # Additional options from kwargs
        for key, value in kwargs.items():
            if key.startswith("--"):
                options.add_argument(f"{key}={value}")
            else:
                options.add_argument(f"--{key}={value}")

        # Get ChromeDriver
        service = ChromeService(ChromeDriverManager().install())

        return webdriver.Chrome(service=service, options=options)

    def _get_firefox_driver(self, headless: bool = True, **kwargs) -> webdriver.Firefox:
        """Get Firefox WebDriver instance."""
        options = FirefoxOptions()

        if headless:
            options.add_argument("--headless")

        # Common Firefox options
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-plugins")
        options.add_argument("--disable-images")
        options.add_argument("--disable-javascript")
        options.add_argument("--disable-web-security")
        options.add_argument("--allow-running-insecure-content")

        # User agent
        user_agent = self.config.get("browser.user_agent")
        if user_agent:
            options.add_argument(f"--user-agent={user_agent}")

        # Download path
        download_path = self.config.get("browser.download_path", "./downloads")
        os.makedirs(download_path, exist_ok=True)

        # Set preferences
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.dir", os.path.abspath(download_path))
        profile.set_preference(
            "browser.helperApps.neverAsk.saveToDisk", "application/pdf,application/zip"
        )

        # Additional options from kwargs
        for key, value in kwargs.items():
            if key.startswith("--"):
                options.add_argument(f"{key}={value}")
            else:
                options.add_argument(f"--{key}={value}")

        # Get GeckoDriver
        service = FirefoxService(GeckoDriverManager().install())

        return webdriver.Firefox(
            service=service, options=options, firefox_profile=profile
        )

    def _get_edge_driver(self, headless: bool = True, **kwargs) -> webdriver.Edge:
        """Get Edge WebDriver instance."""
        options = EdgeOptions()

        if headless:
            options.add_argument("--headless")

        # Common Edge options
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-plugins")
        options.add_argument("--disable-images")
        options.add_argument("--disable-javascript")
        options.add_argument("--disable-web-security")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        # User agent
        user_agent = self.config.get("browser.user_agent")
        if user_agent:
            options.add_argument(f"--user-agent={user_agent}")

        # Download path
        download_path = self.config.get("browser.download_path", "./downloads")
        os.makedirs(download_path, exist_ok=True)
        prefs = {
            "download.default_directory": os.path.abspath(download_path),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
        }
        options.add_experimental_option("prefs", prefs)

        # Additional options from kwargs
        for key, value in kwargs.items():
            if key.startswith("--"):
                options.add_argument(f"{key}={value}")
            else:
                options.add_argument(f"--{key}={value}")

        # Get EdgeDriver
        service = EdgeService(EdgeChromiumDriverManager().install())

        return webdriver.Edge(service=service, options=options)

    def _get_safari_driver(self, **kwargs) -> webdriver.Safari:
        """Get Safari WebDriver instance."""
        # Safari doesn't support headless mode
        service = SafariService()
        return webdriver.Safari(service=service)

    def get_playwright_browser(self, browser: str = "chromium", headless: bool = True):
        """
        Get Playwright browser instance.

        Args:
            browser: Browser type (chromium, firefox, webkit)
            headless: Run in headless mode

        Returns:
            Playwright browser instance
        """
        if not PLAYWRIGHT_AVAILABLE:
            raise ImportError(
                "Playwright is not installed. Install it with: pip install playwright"
            )

        logger.info(f"Initializing Playwright {browser} browser (headless: {headless})")

        playwright = sync_playwright().start()

        if browser == "chromium":
            browser_instance = playwright.chromium.launch(headless=headless)
        elif browser == "firefox":
            browser_instance = playwright.firefox.launch(headless=headless)
        elif browser == "webkit":
            browser_instance = playwright.webkit.launch(headless=headless)
        else:
            raise ValueError(f"Unsupported Playwright browser: {browser}")

        logger.info(f"Playwright browser initialized successfully: {browser}")
        return browser_instance, playwright

    def quit_driver(self):
        """Quit the current WebDriver instance."""
        if self.driver:
            self.driver.quit()
            self.driver = None
            logger.info("WebDriver quit successfully")

    def take_screenshot(self, filename: str = None) -> str:
        """
        Take a screenshot of the current page.

        Args:
            filename: Screenshot filename

        Returns:
            Path to the screenshot file
        """
        if not self.driver:
            raise RuntimeError("No WebDriver instance available")

        if not filename:
            timestamp = int(time.time())
            filename = f"screenshot_{timestamp}.png"

        screenshot_dir = "reports/screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)

        screenshot_path = os.path.join(screenshot_dir, filename)
        self.driver.save_screenshot(screenshot_path)

        logger.info(f"Screenshot saved: {screenshot_path}")
        return screenshot_path

    def get_page_source(self) -> str:
        """Get the current page source."""
        if not self.driver:
            raise RuntimeError("No WebDriver instance available")

        return self.driver.page_source

    def get_current_url(self) -> str:
        """Get the current URL."""
        if not self.driver:
            raise RuntimeError("No WebDriver instance available")

        return self.driver.current_url

    def get_title(self) -> str:
        """Get the current page title."""
        if not self.driver:
            raise RuntimeError("No WebDriver instance available")

        return self.driver.title

    def refresh_page(self):
        """Refresh the current page."""
        if not self.driver:
            raise RuntimeError("No WebDriver instance available")

        self.driver.refresh()
        logger.info("Page refreshed")

    def navigate_back(self):
        """Navigate back in browser history."""
        if not self.driver:
            raise RuntimeError("No WebDriver instance available")

        self.driver.back()
        logger.info("Navigated back")

    def navigate_forward(self):
        """Navigate forward in browser history."""
        if not self.driver:
            raise RuntimeError("No WebDriver instance available")

        self.driver.forward()
        logger.info("Navigated forward")

    def maximize_window(self):
        """Maximize the browser window."""
        if not self.driver:
            raise RuntimeError("No WebDriver instance available")

        self.driver.maximize_window()
        logger.info("Window maximized")

    def minimize_window(self):
        """Minimize the browser window."""
        if not self.driver:
            raise RuntimeError("No WebDriver instance available")

        self.driver.minimize_window()
        logger.info("Window minimized")

    def set_window_size(self, width: int, height: int):
        """Set the browser window size."""
        if not self.driver:
            raise RuntimeError("No WebDriver instance available")

        self.driver.set_window_size(width, height)
        logger.info(f"Window size set to {width}x{height}")

    def get_window_size(self) -> Dict[str, int]:
        """Get the current window size."""
        if not self.driver:
            raise RuntimeError("No WebDriver instance available")

        size = self.driver.get_window_size()
        logger.info(f"Current window size: {size['width']}x{size['height']}")
        return size

    def add_cookie(self, name: str, value: str, domain: str = None, path: str = None):
        """Add a cookie to the browser."""
        if not self.driver:
            raise RuntimeError("No WebDriver instance available")

        cookie = {"name": name, "value": value}
        if domain:
            cookie["domain"] = domain
        if path:
            cookie["path"] = path

        self.driver.add_cookie(cookie)
        logger.info(f"Cookie added: {name}={value}")

    def delete_cookie(self, name: str):
        """Delete a cookie from the browser."""
        if not self.driver:
            raise RuntimeError("No WebDriver instance available")

        self.driver.delete_cookie(name)
        logger.info(f"Cookie deleted: {name}")

    def delete_all_cookies(self):
        """Delete all cookies from the browser."""
        if not self.driver:
            raise RuntimeError("No WebDriver instance available")

        self.driver.delete_all_cookies()
        logger.info("All cookies deleted")

    def get_cookies(self) -> list:
        """Get all cookies from the browser."""
        if not self.driver:
            raise RuntimeError("No WebDriver instance available")

        return self.driver.get_cookies()
