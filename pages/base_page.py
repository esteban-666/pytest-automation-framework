"""
Base page object class with common web element interactions.
"""

import time
from typing import Optional, List, Tuple
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
)
from utils.logger import logger


class BasePage:
    """Base page object class with common web element interactions."""

    def __init__(self, driver):
        """Initialize base page with webdriver."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def find_element(self, locator: Tuple[str, str], timeout: int = 20) -> WebElement:
        """Find element with explicit wait."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            logger.error(f"Element not found within {timeout} seconds: {locator}")
            raise

    def find_elements(
        self, locator: Tuple[str, str], timeout: int = 20
    ) -> List[WebElement]:
        """Find elements with explicit wait."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            logger.error(f"Elements not found within {timeout} seconds: {locator}")
            raise

    def click_element(self, locator: Tuple[str, str], timeout: int = 20):
        """Click element with explicit wait."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except (TimeoutException, ElementClickInterceptedException) as e:
            logger.error(f"Failed to click element within {timeout} seconds: {locator}")
            raise

    def type_text(self, locator: Tuple[str, str], text: str, timeout: int = 20):
        """Type text into element with explicit wait."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.presence_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            logger.error(f"Failed to type text within {timeout} seconds: {locator}")
            raise

    def get_text(self, locator: Tuple[str, str], timeout: int = 20) -> str:
        """Get text from element with explicit wait."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.presence_of_element_located(locator))
            return element.text
        except TimeoutException:
            logger.error(f"Failed to get text within {timeout} seconds: {locator}")
            raise

    def get_attribute(
        self, locator: Tuple[str, str], attribute: str, timeout: int = 20
    ) -> str:
        """Get attribute from element with explicit wait."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.presence_of_element_located(locator))
            return element.get_attribute(attribute)
        except TimeoutException:
            logger.error(f"Failed to get attribute within {timeout} seconds: {locator}")
            raise

    def is_element_present(self, locator: Tuple[str, str], timeout: int = 20) -> bool:
        """Check if element is present with explicit wait."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_element_visible(self, locator: Tuple[str, str], timeout: int = 20) -> bool:
        """Check if element is visible with explicit wait."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_element_clickable(self, locator: Tuple[str, str], timeout: int = 20) -> bool:
        """Check if element is clickable with explicit wait."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False

    def wait_for_element_to_disappear(
        self, locator: Tuple[str, str], timeout: int = 20
    ) -> bool:
        """Wait for element to disappear with explicit wait."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def hover_over_element(self, locator: Tuple[str, str], timeout: int = 20):
        """Hover over element with explicit wait."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.presence_of_element_located(locator))
            from selenium.webdriver.common.action_chains import ActionChains

            ActionChains(self.driver).move_to_element(element).perform()
        except TimeoutException:
            logger.error(
                f"Failed to hover over element within {timeout} seconds: {locator}"
            )
            raise

    def drag_and_drop(
        self,
        source_locator: Tuple[str, str],
        target_locator: Tuple[str, str],
        timeout: int = 20,
    ):
        """Drag and drop element with explicit wait."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            source = wait.until(EC.presence_of_element_located(source_locator))
            target = wait.until(EC.presence_of_element_located(target_locator))
            from selenium.webdriver.common.action_chains import ActionChains

            ActionChains(self.driver).drag_and_drop(source, target).perform()
        except TimeoutException:
            logger.error(f"Failed to drag and drop within {timeout} seconds")
            raise

    def switch_to_frame(self, locator: Tuple[str, str], timeout: int = 20):
        """Switch to frame with explicit wait."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            frame = wait.until(EC.frame_to_be_available_and_switch_to_it(locator))
            return frame
        except TimeoutException:
            logger.error(
                f"Failed to switch to frame within {timeout} seconds: {locator}"
            )
            raise

    def switch_to_default_content(self):
        """Switch back to default content."""
        self.driver.switch_to.default_content()

    def select_option_by_text(
        self, locator: Tuple[str, str], option_text: str, timeout: int = 20
    ):
        """Select dropdown option by text with explicit wait."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.presence_of_element_located(locator))
            from selenium.webdriver.support.ui import Select

            select = Select(element)
            select.select_by_visible_text(option_text)
        except TimeoutException:
            logger.error(
                f"Failed to select option by text within {timeout} seconds: {locator}"
            )
            raise

    def select_option_by_value(
        self, locator: Tuple[str, str], option_value: str, timeout: int = 20
    ):
        """Select dropdown option by value with explicit wait."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.presence_of_element_located(locator))
            from selenium.webdriver.support.ui import Select

            select = Select(element)
            select.select_by_value(option_value)
        except TimeoutException:
            logger.error(
                f"Failed to select option by value within {timeout} seconds: {locator}"
            )
            raise

    def wait_for_page_load(self, timeout: int = 20):
        """Wait for page to load completely."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(
                lambda driver: driver.execute_script("return document.readyState")
                == "complete"
            )
        except TimeoutException:
            logger.error(f"Page did not load completely within {timeout} seconds")
            raise

    def get_page_title(self) -> str:
        """Get page title."""
        return self.driver.title

    def get_current_url(self) -> str:
        """Get current URL."""
        return self.driver.current_url

    def refresh_page(self):
        """Refresh the current page."""
        self.driver.refresh()
        self.wait_for_page_load()

    def go_back(self):
        """Go back to previous page."""
        self.driver.back()
        self.wait_for_page_load()

    def go_forward(self):
        """Go forward to next page."""
        self.driver.forward()
        self.wait_for_page_load()

    def take_screenshot(self, filename: str):
        """Take screenshot and save to file."""
        try:
            self.driver.save_screenshot(filename)
            logger.info(f"Screenshot saved: {filename}")
        except Exception as e:
            logger.error(f"Failed to take screenshot: {e}")

    def scroll_to_element(self, locator: Tuple[str, str], timeout: int = 20):
        """Scroll to element with explicit wait."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        except TimeoutException:
            logger.error(
                f"Failed to scroll to element within {timeout} seconds: {locator}"
            )
            raise

    def scroll_to_bottom(self):
        """Scroll to bottom of page."""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        """Scroll to top of page."""
        self.driver.execute_script("window.scrollTo(0, 0);")

    def wait_for_ajax(self, timeout: int = 20):
        """Wait for AJAX requests to complete."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(
                lambda driver: driver.execute_script("return jQuery.active == 0")
            )
        except TimeoutException:
            logger.warning("AJAX requests did not complete within timeout")
        except Exception:
            # jQuery might not be available
            pass

    def accept_alert(self, timeout: int = 20):
        """Accept alert with explicit wait."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            alert = wait.until(EC.alert_is_present())
            alert.accept()
        except TimeoutException:
            logger.error(f"Alert not present within {timeout} seconds")
            raise

    def dismiss_alert(self, timeout: int = 20):
        """Dismiss alert with explicit wait."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            alert = wait.until(EC.alert_is_present())
            alert.dismiss()
        except TimeoutException:
            logger.error(f"Alert not present within {timeout} seconds")
            raise

    def get_alert_text(self, timeout: int = 20) -> str:
        """Get alert text with explicit wait."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            alert = wait.until(EC.alert_is_present())
            return alert.text
        except TimeoutException:
            logger.error(f"Alert not present within {timeout} seconds")
            raise

    def send_keys_to_alert(self, text: str, timeout: int = 20):
        """Send keys to alert with explicit wait."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            alert = wait.until(EC.alert_is_present())
            alert.send_keys(text)
            alert.accept()
        except TimeoutException:
            logger.error(f"Alert not present within {timeout} seconds")
            raise
