"""
Page objects for The Internet (Herokuapp) practice site.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TheInternetMainPage(BasePage):
    """Main page object for The Internet."""

    # Locators - using shorter CSS selectors
    FORM_AUTHENTICATION_LINK = (By.CSS_SELECTOR, "a[href='/login']")
    DYNAMIC_CONTENT_LINK = (By.CSS_SELECTOR, "a[href='/dynamic_content']")
    DYNAMIC_LOADING_LINK = (By.CSS_SELECTOR, "a[href='/dynamic_loading']")
    FILE_UPLOAD_LINK = (By.CSS_SELECTOR, "a[href='/upload']")
    CHECKBOXES_LINK = (By.CSS_SELECTOR, "a[href='/checkboxes']")
    DROPDOWN_LINK = (By.CSS_SELECTOR, "a[href='/dropdown']")
    JAVASCRIPT_ALERTS_LINK = (By.CSS_SELECTOR, "a[href='/javascript_alerts']")
    FRAMES_LINK = (By.CSS_SELECTOR, "a[href='/frames']")
    TABLES_LINK = (By.CSS_SELECTOR, "a[href='/tables']")

    def click_form_authentication(self):
        """Click on Form Authentication link."""
        self.click_element(self.FORM_AUTHENTICATION_LINK, timeout=20)
        return TheInternetLoginPage(self.driver)

    def click_dynamic_content(self):
        """Click on Dynamic Content link."""
        self.click_element(self.DYNAMIC_CONTENT_LINK, timeout=20)
        return TheInternetDynamicContentPage(self.driver)

    def click_dynamic_loading(self):
        """Click on Dynamic Loading link."""
        self.click_element(self.DYNAMIC_LOADING_LINK, timeout=20)
        return TheInternetDynamicLoadingPage(self.driver)

    def click_file_upload(self):
        """Click on File Upload link."""
        self.click_element(self.FILE_UPLOAD_LINK, timeout=20)
        return TheInternetFileUploadPage(self.driver)

    def click_checkboxes(self):
        """Click on Checkboxes link."""
        self.click_element(self.CHECKBOXES_LINK, timeout=20)
        return TheInternetCheckboxesPage(self.driver)

    def click_dropdown(self):
        """Click on Dropdown link."""
        self.click_element(self.DROPDOWN_LINK, timeout=20)
        return TheInternetDropdownPage(self.driver)

    def click_javascript_alerts(self):
        """Click on JavaScript Alerts link."""
        self.click_element(self.JAVASCRIPT_ALERTS_LINK, timeout=20)
        return TheInternetJavaScriptAlertsPage(self.driver)

    def click_frames(self):
        """Click on Frames link."""
        self.click_element(self.FRAMES_LINK, timeout=20)
        return TheInternetFramesPage(self.driver)

    def click_tables(self):
        """Click on Sortable Data Tables link."""
        self.click_element(self.TABLES_LINK, timeout=20)
        return TheInternetTablesPage(self.driver)


class TheInternetLoginPage(BasePage):
    """Login page object for The Internet."""

    # Locators - using shorter CSS selectors
    USERNAME_INPUT = (By.CSS_SELECTOR, "#username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".radius")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".button")
    FLASH_MESSAGE = (By.CSS_SELECTOR, "#flash")
    SUBHEADER = (By.CSS_SELECTOR, ".subheader")

    def login(self, username, password):
        """Perform login."""
        self.type_text(self.USERNAME_INPUT, username, timeout=20)
        self.type_text(self.PASSWORD_INPUT, password, timeout=20)
        self.click_element(self.LOGIN_BUTTON, timeout=20)

    def logout(self):
        """Perform logout."""
        self.click_element(self.LOGOUT_BUTTON, timeout=20)

    def get_flash_message(self):
        """Get flash message text."""
        return self.get_text(self.FLASH_MESSAGE, timeout=20)

    def is_flash_message_present(self):
        """Check if flash message is present."""
        return self.is_element_present(self.FLASH_MESSAGE, timeout=20)

    def get_subheader_text(self):
        """Get subheader text."""
        return self.get_text(self.SUBHEADER, timeout=20)

    def is_logged_in(self):
        """Check if user is logged in."""
        return self.is_element_present(self.LOGOUT_BUTTON, timeout=20)


class TheInternetDynamicContentPage(BasePage):
    """Dynamic Content page object for The Internet."""

    # Locators - using shorter CSS selectors
    CONTENT_DIVS = (By.CSS_SELECTOR, ".large-10")
    REFRESH_BUTTON = (By.CSS_SELECTOR, "a[href='/dynamic_content?with_content=static']")

    def get_content_texts(self):
        """Get all content text elements."""
        elements = self.find_elements(self.CONTENT_DIVS, timeout=20)
        return [element.text for element in elements]

    def click_refresh(self):
        """Click refresh button."""
        self.click_element(self.REFRESH_BUTTON, timeout=20)

    def wait_for_page_load(self):
        """Wait for page to load after refresh."""
        self.wait_for_page_load()


class TheInternetDynamicLoadingPage(BasePage):
    """Dynamic Loading page object for The Internet."""

    # Locators - using shorter CSS selectors
    EXAMPLE_1_LINK = (By.CSS_SELECTOR, "a[href='/dynamic_loading/1']")
    EXAMPLE_2_LINK = (By.CSS_SELECTOR, "a[href='/dynamic_loading/2']")
    START_BUTTON = (By.CSS_SELECTOR, "#start button")
    LOADING_ELEMENT = (By.CSS_SELECTOR, "#loading")
    FINISH_ELEMENT = (By.CSS_SELECTOR, "#finish")

    def click_example_1(self):
        """Click on Example 1 link."""
        self.click_element(self.EXAMPLE_1_LINK, timeout=20)
        return TheInternetDynamicLoadingExamplePage(self.driver)

    def click_example_2(self):
        """Click on Example 2 link."""
        self.click_element(self.EXAMPLE_2_LINK, timeout=20)
        return TheInternetDynamicLoadingExamplePage(self.driver)


class TheInternetDynamicLoadingExamplePage(BasePage):
    """Dynamic Loading Example page object for The Internet."""

    # Locators - using shorter CSS selectors
    START_BUTTON = (By.CSS_SELECTOR, "#start button")
    LOADING_ELEMENT = (By.CSS_SELECTOR, "#loading")
    FINISH_ELEMENT = (By.CSS_SELECTOR, "#finish")

    def click_start(self):
        """Click start button."""
        self.click_element(self.START_BUTTON, timeout=20)

    def wait_for_loading_to_finish(self, timeout=30):
        """Wait for loading to finish."""
        return self.wait_for_element_to_disappear(self.LOADING_ELEMENT, timeout)

    def get_finish_text(self):
        """Get finish text."""
        return self.get_text(self.FINISH_ELEMENT, timeout=20)

    def is_finish_visible(self):
        """Check if finish element is visible."""
        return self.is_element_visible(self.FINISH_ELEMENT, timeout=20)


class TheInternetFileUploadPage(BasePage):
    """File Upload page object for The Internet."""

    # Locators - using shorter CSS selectors
    FILE_INPUT = (By.CSS_SELECTOR, "#file-upload")
    UPLOAD_BUTTON = (By.CSS_SELECTOR, "#file-submit")
    UPLOADED_FILES = (By.CSS_SELECTOR, "#uploaded-files")
    DRAG_DROP_AREA = (By.CSS_SELECTOR, "#drag-drop-upload")

    def upload_file(self, file_path):
        """Upload a file."""
        self.type_text(self.FILE_INPUT, file_path, timeout=20)
        self.click_element(self.UPLOAD_BUTTON, timeout=20)

    def get_uploaded_file_name(self):
        """Get uploaded file name."""
        return self.get_text(self.UPLOADED_FILES, timeout=20)

    def drag_and_drop_file(self, file_path):
        """Drag and drop a file."""
        # This would require JavaScript execution for drag and drop
        self.driver.execute_script(
            f"arguments[0].files = [new File([''], '{file_path}')]",
            self.find_element(self.FILE_INPUT, timeout=20),
        )


class TheInternetCheckboxesPage(BasePage):
    """Checkboxes page object for The Internet."""

    # Locators - using shorter CSS selectors
    CHECKBOX_1 = (By.CSS_SELECTOR, "input[type='checkbox']:first-of-type")
    CHECKBOX_2 = (By.CSS_SELECTOR, "input[type='checkbox']:last-of-type")

    def click_checkbox_1(self):
        """Click first checkbox."""
        self.click_element(self.CHECKBOX_1, timeout=20)

    def click_checkbox_2(self):
        """Click second checkbox."""
        self.click_element(self.CHECKBOX_2, timeout=20)

    def is_checkbox_1_checked(self):
        """Check if first checkbox is checked."""
        element = self.find_element(self.CHECKBOX_1, timeout=20)
        return element.is_selected()

    def is_checkbox_2_checked(self):
        """Check if second checkbox is checked."""
        element = self.find_element(self.CHECKBOX_2, timeout=20)
        return element.is_selected()

    def check_all_checkboxes(self):
        """Check all checkboxes."""
        if not self.is_checkbox_1_checked():
            self.click_checkbox_1()
        if not self.is_checkbox_2_checked():
            self.click_checkbox_2()

    def uncheck_all_checkboxes(self):
        """Uncheck all checkboxes."""
        if self.is_checkbox_1_checked():
            self.click_checkbox_1()
        if self.is_checkbox_2_checked():
            self.click_checkbox_2()


class TheInternetDropdownPage(BasePage):
    """Dropdown page object for The Internet."""

    # Locators - using shorter CSS selectors
    DROPDOWN = (By.CSS_SELECTOR, "#dropdown")

    def select_option_by_text(self, option_text):
        """Select dropdown option by text."""
        self.select_option_by_text(self.DROPDOWN, option_text, timeout=20)

    def select_option_by_value(self, option_value):
        """Select dropdown option by value."""
        self.select_option_by_value(self.DROPDOWN, option_value, timeout=20)

    def get_selected_option_text(self):
        """Get selected option text."""
        from selenium.webdriver.support.ui import Select

        dropdown = Select(self.find_element(self.DROPDOWN, timeout=20))
        return dropdown.first_selected_option.text

    def get_all_options(self):
        """Get all dropdown options."""
        from selenium.webdriver.support.ui import Select

        dropdown = Select(self.find_element(self.DROPDOWN, timeout=20))
        return [option.text for option in dropdown.options]


class TheInternetJavaScriptAlertsPage(BasePage):
    """JavaScript Alerts page object for The Internet."""

    # Locators - using shorter CSS selectors
    JS_ALERT_BUTTON = (By.CSS_SELECTOR, "button[onclick='jsAlert()']")
    JS_CONFIRM_BUTTON = (By.CSS_SELECTOR, "button[onclick='jsConfirm()']")
    JS_PROMPT_BUTTON = (By.CSS_SELECTOR, "button[onclick='jsPrompt()']")
    RESULT = (By.CSS_SELECTOR, "#result")

    def click_js_alert(self):
        """Click JS Alert button."""
        self.click_element(self.JS_ALERT_BUTTON, timeout=20)

    def click_js_confirm(self):
        """Click JS Confirm button."""
        self.click_element(self.JS_CONFIRM_BUTTON, timeout=20)

    def click_js_prompt(self):
        """Click JS Prompt button."""
        self.click_element(self.JS_PROMPT_BUTTON, timeout=20)

    def get_result_text(self):
        """Get result text."""
        return self.get_text(self.RESULT, timeout=20)

    def accept_alert(self):
        """Accept alert."""
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """Dismiss alert."""
        self.driver.switch_to.alert.dismiss()

    def send_keys_to_alert(self, text):
        """Send keys to prompt alert."""
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()


class TheInternetFramesPage(BasePage):
    """Frames page object for The Internet."""

    # Locators - using shorter CSS selectors
    NESTED_FRAMES_LINK = (By.CSS_SELECTOR, "a[href='/nested_frames']")
    IFRAME_LINK = (By.CSS_SELECTOR, "a[href='/iframe']")

    def click_nested_frames(self):
        """Click on Nested Frames link."""
        self.click_element(self.NESTED_FRAMES_LINK, timeout=20)
        return TheInternetNestedFramesPage(self.driver)

    def click_iframe(self):
        """Click on iFrame link."""
        self.click_element(self.IFRAME_LINK, timeout=20)
        return TheInternetIframePage(self.driver)


class TheInternetNestedFramesPage(BasePage):
    """Nested Frames page object for The Internet."""

    # Locators - using shorter CSS selectors
    FRAME_TOP = (By.CSS_SELECTOR, "frame[name='frame-top']")
    FRAME_LEFT = (By.CSS_SELECTOR, "frame[name='frame-left']")
    FRAME_MIDDLE = (By.CSS_SELECTOR, "frame[name='frame-middle']")
    FRAME_RIGHT = (By.CSS_SELECTOR, "frame[name='frame-right']")
    FRAME_BOTTOM = (By.CSS_SELECTOR, "frame[name='frame-bottom']")
    BODY = (By.CSS_SELECTOR, "body")

    def switch_to_top_frame(self):
        """Switch to top frame."""
        self.switch_to_frame(self.FRAME_TOP, timeout=20)

    def switch_to_left_frame(self):
        """Switch to left frame."""
        self.switch_to_frame(self.FRAME_LEFT, timeout=20)

    def switch_to_middle_frame(self):
        """Switch to middle frame."""
        self.switch_to_frame(self.FRAME_MIDDLE, timeout=20)

    def switch_to_right_frame(self):
        """Switch to right frame."""
        self.switch_to_frame(self.FRAME_RIGHT, timeout=20)

    def switch_to_bottom_frame(self):
        """Switch to bottom frame."""
        self.switch_to_frame(self.FRAME_BOTTOM, timeout=20)

    def get_frame_text(self):
        """Get text from current frame."""
        return self.get_text(self.BODY, timeout=20)

    def switch_to_default_content(self):
        """Switch back to default content."""
        self.switch_to_default_content()


class TheInternetIframePage(BasePage):
    """iFrame page object for The Internet."""

    # Locators - using shorter CSS selectors
    IFRAME = (By.CSS_SELECTOR, "#mce_0_ifr")
    EDITOR = (By.CSS_SELECTOR, "#tinymce")

    def switch_to_iframe(self):
        """Switch to iframe."""
        self.switch_to_frame(self.IFRAME, timeout=20)

    def get_editor_text(self):
        """Get text from editor."""
        return self.get_text(self.EDITOR, timeout=20)

    def type_in_editor(self, text):
        """Type text in editor."""
        self.type_text(self.EDITOR, text, timeout=20)

    def clear_editor(self):
        """Clear editor content."""
        element = self.find_element(self.EDITOR, timeout=20)
        element.clear()


class TheInternetTablesPage(BasePage):
    """Sortable Data Tables page object for The Internet."""

    # Locators - using shorter CSS selectors
    TABLE_1 = (By.CSS_SELECTOR, "#table1")
    TABLE_2 = (By.CSS_SELECTOR, "#table2")
    TABLE_HEADERS = (By.CSS_SELECTOR, "th")
    TABLE_ROWS = (By.CSS_SELECTOR, "tr")

    def get_table_headers(self, table_id=1):
        """Get table headers."""
        if table_id == 1:
            table = self.find_element(self.TABLE_1, timeout=20)
        else:
            table = self.find_element(self.TABLE_2, timeout=20)

        headers = table.find_elements(By.CSS_SELECTOR, "th")
        return [header.text for header in headers]

    def get_table_data(self, table_id=1):
        """Get table data."""
        if table_id == 1:
            table = self.find_element(self.TABLE_1, timeout=20)
        else:
            table = self.find_element(self.TABLE_2, timeout=20)

        rows = table.find_elements(By.CSS_SELECTOR, "tr")[1:]  # Skip header row
        data = []
        for row in rows:
            cells = row.find_elements(By.CSS_SELECTOR, "td")
            data.append([cell.text for cell in cells])
        return data

    def click_header_to_sort(self, header_text, table_id=1):
        """Click header to sort table."""
        if table_id == 1:
            table = self.find_element(self.TABLE_1, timeout=20)
        else:
            table = self.find_element(self.TABLE_2, timeout=20)

        header = table.find_element(By.XPATH, f".//th[text()='{header_text}']")
        header.click()

    def get_row_count(self, table_id=1):
        """Get number of data rows in table."""
        data = self.get_table_data(table_id)
        return len(data)
