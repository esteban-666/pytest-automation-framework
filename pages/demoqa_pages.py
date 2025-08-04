"""
Page objects for DemoQA practice site.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DemoQAMainPage(BasePage):
    """Main page object for DemoQA."""
    
    # Locators - using proper selectors
    ELEMENTS_CARD = (By.XPATH, "//div[contains(@class, 'card-body')]//h5[text()='Elements']")
    FORMS_CARD = (By.XPATH, "//div[contains(@class, 'card-body')]//h5[text()='Forms']")
    WIDGETS_CARD = (By.XPATH, "//div[contains(@class, 'card-body')]//h5[text()='Widgets']")
    INTERACTIONS_CARD = (By.XPATH, "//div[contains(@class, 'card-body')]//h5[text()='Interactions']")
    BOOK_STORE_CARD = (By.XPATH, "//div[contains(@class, 'card-body')]//h5[text()='Book Store Application']")
    
    def navigate_to_elements(self):
        """Navigate to Elements section."""
        self.click_element(self.ELEMENTS_CARD, timeout=20)
        return DemoQAElementsPage(self.driver)
    
    def navigate_to_forms(self):
        """Navigate to Forms section."""
        self.click_element(self.FORMS_CARD, timeout=20)
        return DemoQAFormsPage(self.driver)
    
    def navigate_to_widgets(self):
        """Navigate to Widgets section."""
        self.click_element(self.WIDGETS_CARD, timeout=20)
        return DemoQAWidgetsPage(self.driver)
    
    def navigate_to_interactions(self):
        """Navigate to Interactions section."""
        self.click_element(self.INTERACTIONS_CARD, timeout=20)
        return DemoQAInteractionsPage(self.driver)
    
    def navigate_to_book_store(self):
        """Navigate to Book Store Application."""
        self.click_element(self.BOOK_STORE_CARD, timeout=20)
        return DemoQABookStorePage(self.driver)


class DemoQAElementsPage(BasePage):
    """Elements page object for DemoQA."""
    
    # Locators - using proper selectors
    TEXT_BOX_MENU = (By.XPATH, "//span[text()='Text Box']")
    CHECK_BOX_MENU = (By.XPATH, "//span[text()='Check Box']")
    RADIO_BUTTON_MENU = (By.XPATH, "//span[text()='Radio Button']")
    WEB_TABLES_MENU = (By.XPATH, "//span[text()='Web Tables']")
    BUTTONS_MENU = (By.XPATH, "//span[text()='Buttons']")
    LINKS_MENU = (By.XPATH, "//span[text()='Links']")
    BROKEN_LINKS_MENU = (By.XPATH, "//span[text()='Broken Links']")
    UPLOAD_DOWNLOAD_MENU = (By.XPATH, "//span[text()='Upload and Download']")
    DYNAMIC_PROPERTIES_MENU = (By.XPATH, "//span[text()='Dynamic Properties']")
    
    def click_text_box(self):
        """Click on Text Box menu item."""
        self.click_element(self.TEXT_BOX_MENU, timeout=20)
        return DemoQATextBoxPage(self.driver)
    
    def click_dynamic_properties(self):
        """Click on Dynamic Properties menu item."""
        self.click_element(self.DYNAMIC_PROPERTIES_MENU, timeout=20)
        return DemoQADynamicPropertiesPage(self.driver)


class DemoQATextBoxPage(BasePage):
    """Text Box page object for DemoQA."""
    
    # Locators - using proper CSS selectors
    FULL_NAME_INPUT = (By.CSS_SELECTOR, "#userName")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#userEmail")
    CURRENT_ADDRESS_INPUT = (By.CSS_SELECTOR, "#currentAddress")
    PERMANENT_ADDRESS_INPUT = (By.CSS_SELECTOR, "#permanentAddress")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")
    OUTPUT_DIV = (By.CSS_SELECTOR, "#output")
    
    def fill_form(self, full_name, email, current_address, permanent_address):
        """Fill the text box form."""
        self.type_text(self.FULL_NAME_INPUT, full_name, timeout=20)
        self.type_text(self.EMAIL_INPUT, email, timeout=20)
        self.type_text(self.CURRENT_ADDRESS_INPUT, current_address, timeout=20)
        self.type_text(self.PERMANENT_ADDRESS_INPUT, permanent_address, timeout=20)
    
    def submit_form(self):
        """Submit the form."""
        self.click_element(self.SUBMIT_BUTTON, timeout=20)
    
    def get_output_text(self):
        """Get the output text after form submission."""
        return self.get_text(self.OUTPUT_DIV, timeout=20)
    
    def is_output_present(self):
        """Check if output is present."""
        return self.is_element_present(self.OUTPUT_DIV, timeout=20)


class DemoQADynamicPropertiesPage(BasePage):
    """Dynamic Properties page object for DemoQA."""
    
    # Locators - using proper CSS selectors
    ENABLE_AFTER_BUTTON = (By.CSS_SELECTOR, "#enableAfter")
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, "#colorChange")
    VISIBLE_AFTER_BUTTON = (By.CSS_SELECTOR, "#visibleAfter")
    
    def wait_for_button_enabled(self, timeout=20):
        """Wait for button to be enabled."""
        return self.is_element_clickable(self.ENABLE_AFTER_BUTTON, timeout)
    
    def click_enabled_button(self):
        """Click the enabled button."""
        self.click_element(self.ENABLE_AFTER_BUTTON, timeout=20)
    
    def get_color_button_color(self):
        """Get the color of the color change button."""
        element = self.find_element(self.COLOR_CHANGE_BUTTON, timeout=20)
        return element.value_of_css_property("color")
    
    def wait_for_visible_button(self, timeout=20):
        """Wait for button to become visible."""
        return self.is_element_visible(self.VISIBLE_AFTER_BUTTON, timeout)


class DemoQAFormsPage(BasePage):
    """Forms page object for DemoQA."""
    
    # Locators - using proper selectors
    PRACTICE_FORM_MENU = (By.XPATH, "//span[text()='Practice Form']")
    
    def click_practice_form(self):
        """Click on Practice Form menu item."""
        self.click_element(self.PRACTICE_FORM_MENU, timeout=20)
        return DemoQAPracticeFormPage(self.driver)


class DemoQAPracticeFormPage(BasePage):
    """Practice Form page object for DemoQA."""
    
    # Locators - using proper CSS selectors
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#firstName")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#lastName")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#userEmail")
    GENDER_MALE_RADIO = (By.CSS_SELECTOR, "input[value='Male']")
    GENDER_FEMALE_RADIO = (By.CSS_SELECTOR, "input[value='Female']")
    GENDER_OTHER_RADIO = (By.CSS_SELECTOR, "input[value='Other']")
    MOBILE_INPUT = (By.CSS_SELECTOR, "#userNumber")
    DATE_OF_BIRTH_INPUT = (By.CSS_SELECTOR, "#dateOfBirthInput")
    SUBJECTS_INPUT = (By.CSS_SELECTOR, "#subjectsInput")
    HOBBIES_SPORTS_CHECKBOX = (By.CSS_SELECTOR, "input[value='Sports']")
    HOBBIES_READING_CHECKBOX = (By.CSS_SELECTOR, "input[value='Reading']")
    HOBBIES_MUSIC_CHECKBOX = (By.CSS_SELECTOR, "input[value='Music']")
    UPLOAD_PICTURE_INPUT = (By.CSS_SELECTOR, "#uploadPicture")
    CURRENT_ADDRESS_INPUT = (By.CSS_SELECTOR, "#currentAddress")
    STATE_DROPDOWN = (By.CSS_SELECTOR, "#state")
    CITY_DROPDOWN = (By.CSS_SELECTOR, "#city")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")
    MODAL_TITLE = (By.CSS_SELECTOR, ".modal-title")
    MODAL_CONTENT = (By.CSS_SELECTOR, ".modal-content")
    
    def fill_personal_info(self, first_name, last_name, email, gender="Male"):
        """Fill personal information."""
        self.type_text(self.FIRST_NAME_INPUT, first_name, timeout=20)
        self.type_text(self.LAST_NAME_INPUT, last_name, timeout=20)
        self.type_text(self.EMAIL_INPUT, email, timeout=20)
        
        if gender == "Male":
            self.click_element(self.GENDER_MALE_RADIO, timeout=20)
        elif gender == "Female":
            self.click_element(self.GENDER_FEMALE_RADIO, timeout=20)
        elif gender == "Other":
            self.click_element(self.GENDER_OTHER_RADIO, timeout=20)
    
    def fill_contact_info(self, mobile):
        """Fill contact information."""
        self.type_text(self.MOBILE_INPUT, mobile, timeout=20)
    
    def select_hobbies(self, hobbies):
        """Select hobbies."""
        if "Sports" in hobbies:
            self.click_element(self.HOBBIES_SPORTS_CHECKBOX, timeout=20)
        if "Reading" in hobbies:
            self.click_element(self.HOBBIES_READING_CHECKBOX, timeout=20)
        if "Music" in hobbies:
            self.click_element(self.HOBBIES_MUSIC_CHECKBOX, timeout=20)
    
    def fill_address(self, address):
        """Fill current address."""
        self.type_text(self.CURRENT_ADDRESS_INPUT, address, timeout=20)
    
    def submit_form(self):
        """Submit the form."""
        self.click_element(self.SUBMIT_BUTTON, timeout=20)
    
    def is_modal_present(self):
        """Check if submission modal is present."""
        return self.is_element_present(self.MODAL_CONTENT, timeout=20)
    
    def get_modal_title(self):
        """Get modal title text."""
        return self.get_text(self.MODAL_TITLE, timeout=20)


class DemoQAInteractionsPage(BasePage):
    """Interactions page object for DemoQA."""
    
    # Locators - using proper selectors
    DRAGGABLE_MENU = (By.XPATH, "//span[text()='Dragabble']")
    DROPPABLE_MENU = (By.XPATH, "//span[text()='Droppable']")
    
    def click_droppable(self):
        """Click on Droppable menu item."""
        self.click_element(self.DROPPABLE_MENU, timeout=20)
        return DemoQADroppablePage(self.driver)


class DemoQADroppablePage(BasePage):
    """Droppable page object for DemoQA."""
    
    # Locators - using proper CSS selectors
    DRAGGABLE_ELEMENT = (By.CSS_SELECTOR, "#draggable")
    DROPPABLE_ELEMENT = (By.CSS_SELECTOR, "#droppable")
    
    def perform_drag_and_drop(self):
        """Perform drag and drop operation."""
        self.drag_and_drop(self.DRAGGABLE_ELEMENT, self.DROPPABLE_ELEMENT, timeout=20)
    
    def get_droppable_text(self):
        """Get text from droppable element."""
        return self.get_text(self.DROPPABLE_ELEMENT, timeout=20)


class DemoQAWidgetsPage(BasePage):
    """Widgets page object for DemoQA."""
    
    # Locators - using proper selectors
    ACCORDIAN_MENU = (By.XPATH, "//span[text()='Accordian']")
    AUTO_COMPLETE_MENU = (By.XPATH, "//span[text()='Auto Complete']")
    DATE_PICKER_MENU = (By.XPATH, "//span[text()='Date Picker']")
    SLIDER_MENU = (By.XPATH, "//span[text()='Slider']")
    PROGRESS_BAR_MENU = (By.XPATH, "//span[text()='Progress Bar']")
    TABS_MENU = (By.XPATH, "//span[text()='Tabs']")
    TOOL_TIPS_MENU = (By.XPATH, "//span[text()='Tool Tips']")
    MENU_MENU = (By.XPATH, "//span[text()='Menu']")
    SELECT_MENU_MENU = (By.XPATH, "//span[text()='Select Menu']")
    
    def click_progress_bar(self):
        """Click on Progress Bar menu item."""
        self.click_element(self.PROGRESS_BAR_MENU, timeout=20)
        return DemoQAProgressBarPage(self.driver)
    
    def click_tabs(self):
        """Click on Tabs menu item."""
        self.click_element(self.TABS_MENU, timeout=20)
        return DemoQATabsPage(self.driver)
    
    def click_tool_tips(self):
        """Click on Tool Tips menu item."""
        self.click_element(self.TOOL_TIPS_MENU, timeout=20)
        return DemoQAToolTipsPage(self.driver)


class DemoQAProgressBarPage(BasePage):
    """Progress Bar page object for DemoQA."""
    
    # Locators - using proper CSS selectors
    START_STOP_BUTTON = (By.CSS_SELECTOR, "#startStopButton")
    PROGRESS_BAR = (By.CSS_SELECTOR, ".progress-bar")
    RESET_BUTTON = (By.CSS_SELECTOR, "#resetButton")
    
    def start_progress(self):
        """Start the progress bar."""
        self.click_element(self.START_STOP_BUTTON, timeout=20)
    
    def wait_for_progress_completion(self, timeout=30):
        """Wait for progress to complete."""
        return self.wait_for_element_to_disappear(self.PROGRESS_BAR, timeout)
    
    def get_progress_text(self):
        """Get progress bar text."""
        return self.get_text(self.PROGRESS_BAR, timeout=20)
    
    def reset_progress(self):
        """Reset the progress bar."""
        self.click_element(self.RESET_BUTTON, timeout=20)


class DemoQATabsPage(BasePage):
    """Tabs page object for DemoQA."""
    
    # Locators - using proper CSS selectors
    WHAT_TAB = (By.CSS_SELECTOR, "#demo-tab-what")
    ORIGIN_TAB = (By.CSS_SELECTOR, "#demo-tab-origin")
    USE_TAB = (By.CSS_SELECTOR, "#demo-tab-use")
    WHAT_CONTENT = (By.CSS_SELECTOR, "#demo-tabpane-what")
    ORIGIN_CONTENT = (By.CSS_SELECTOR, "#demo-tabpane-origin")
    USE_CONTENT = (By.CSS_SELECTOR, "#demo-tabpane-use")
    
    def click_what_tab(self):
        """Click on What tab."""
        self.click_element(self.WHAT_TAB, timeout=20)
    
    def click_origin_tab(self):
        """Click on Origin tab."""
        self.click_element(self.ORIGIN_TAB, timeout=20)
    
    def click_use_tab(self):
        """Click on Use tab."""
        self.click_element(self.USE_TAB, timeout=20)
    
    def is_what_content_visible(self):
        """Check if What content is visible."""
        return self.is_element_visible(self.WHAT_CONTENT, timeout=20)
    
    def is_origin_content_visible(self):
        """Check if Origin content is visible."""
        return self.is_element_visible(self.ORIGIN_CONTENT, timeout=20)
    
    def is_use_content_visible(self):
        """Check if Use content is visible."""
        return self.is_element_visible(self.USE_CONTENT, timeout=20)


class DemoQAToolTipsPage(BasePage):
    """Tool Tips page object for DemoQA."""
    
    # Locators - using proper CSS selectors
    TOOL_TIP_BUTTON = (By.CSS_SELECTOR, "#toolTipButton")
    TOOL_TIP_INNER = (By.CSS_SELECTOR, ".tooltip-inner")
    
    def hover_over_button(self):
        """Hover over the tooltip button."""
        self.hover_over_element(self.TOOL_TIP_BUTTON, timeout=20)
    
    def is_tooltip_present(self):
        """Check if tooltip is present."""
        return self.is_element_present(self.TOOL_TIP_INNER, timeout=20)
    
    def get_tooltip_text(self):
        """Get tooltip text."""
        return self.get_text(self.TOOL_TIP_INNER, timeout=20)


class DemoQABookStorePage(BasePage):
    """Book Store page object for DemoQA."""
    
    # Locators - using proper CSS selectors
    SEARCH_BOX = (By.CSS_SELECTOR, "#searchBox")
    BOOK_TABLE_ROW = (By.CSS_SELECTOR, ".rt-tr-group")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login")
    USERNAME_INPUT = (By.CSS_SELECTOR, "#userName")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#login")
    USER_NAME_DISPLAY = (By.CSS_SELECTOR, "#userName-value")
    
    def search_book(self, search_term):
        """Search for a book."""
        self.type_text(self.SEARCH_BOX, search_term, timeout=20)
    
    def get_book_rows(self):
        """Get all book table rows."""
        return self.find_elements(self.BOOK_TABLE_ROW, timeout=20)
    
    def click_first_book(self):
        """Click on the first book in the table."""
        books = self.get_book_rows()
        if books:
            self.click_element(self.BOOK_TABLE_ROW, timeout=20)
    
    def click_login(self):
        """Click on login button."""
        self.click_element(self.LOGIN_BUTTON, timeout=20)
    
    def login(self, username, password):
        """Perform login."""
        self.type_text(self.USERNAME_INPUT, username, timeout=20)
        self.type_text(self.PASSWORD_INPUT, password, timeout=20)
        self.click_element(self.LOGIN_SUBMIT_BUTTON, timeout=20)
    
    def get_user_name_display(self):
        """Get displayed username after login."""
        return self.get_text(self.USER_NAME_DISPLAY, timeout=20) 