"""
E2E tests for DemoQA practice site.
"""

import pytest
import os
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TestDemoQA:
    """Test cases for DemoQA practice site."""

    @pytest.fixture(autouse=True)
    def setup_page(self, driver):
        """Setup page object for tests."""
        print("\n🔧 Setting up DemoQA page object...")
        self.page = BasePage(driver)
        self.driver = driver
        print("✅ DemoQA page object initialized successfully")

    def log_step(self, step_name, description, expected_result=None):
        """Log test step details to console."""
        print(f"\n📋 {step_name}")
        print(f"   Description: {description}")
        if expected_result:
            print(f"   Expected: {expected_result}")

    def log_page_html(self, test_name):
        """Log page HTML for debugging."""
        try:
            html = self.driver.page_source
            log_file = f"logs/{test_name}_page.html"
            os.makedirs("logs", exist_ok=True)
            with open(log_file, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"📄 Page HTML logged to: {log_file}")
        except Exception as e:
            print(f"❌ Failed to log HTML: {e}")

    def testFormSubmission(self):
        """
        Test form submission on DemoQA practice form
        """
        print("\n" + "=" * 80)
        print("🧪 TEST: DemoQA Practice Form Submission")
        print("=" * 80)

        try:
            # ===== STEP 1: NAVIGATE TO PRACTICE FORM =====
            self.log_step(
                "STEP 1", "Navigate to DemoQA practice form", "Practice form page loads"
            )
            print("   🌐 Navigating to https://demoqa.com/automation-practice-form")
            self.driver.get("https://demoqa.com/automation-practice-form")
            print("   ✅ Practice form page loaded")

            # ===== STEP 2: FILL PERSONAL INFORMATION =====
            self.log_step(
                "STEP 2",
                "Fill personal information fields",
                "All personal fields populated",
            )
            print("   📝 Filling personal information...")

            print("   👤 Entering first name: John")
            self.page.type_text((By.ID, "firstName"), "John")

            print("   👤 Entering last name: Doe")
            self.page.type_text((By.ID, "lastName"), "Doe")

            print("   📧 Entering email: john.doe@example.com")
            self.page.type_text((By.ID, "userEmail"), "john.doe@example.com")
            print("   ✅ Personal information filled")

            # ===== STEP 3: SELECT GENDER =====
            self.log_step("STEP 3", "Select gender option", "Male gender selected")
            print("   👨 Selecting gender: Male")
            self.page.click_element((By.XPATH, "//input[@value='Male']"))
            print("   ✅ Gender selected")

            # ===== STEP 4: ENTER MOBILE NUMBER =====
            self.log_step(
                "STEP 4", "Enter mobile number", "Mobile number field populated"
            )
            print("   📱 Entering mobile number: 1234567890")
            self.page.type_text((By.ID, "userNumber"), "1234567890")
            print("   ✅ Mobile number entered")

            # ===== STEP 5: SELECT DATE OF BIRTH =====
            self.log_step("STEP 5", "Select date of birth", "Date picker opened")
            print("   📅 Opening date picker...")
            self.page.click_element((By.ID, "dateOfBirthInput"))
            print("   ✅ Date picker opened (date selection logic to be implemented)")

            # ===== STEP 6: SELECT SUBJECTS =====
            self.log_step(
                "STEP 6", "Select subjects", "Computer Science subject selected"
            )
            print("   📚 Entering subject: Computer Science")
            self.page.type_text((By.ID, "subjectsInput"), "Computer Science")
            print("   ✅ Subject entered")

            # ===== STEP 7: SELECT HOBBIES =====
            self.log_step("STEP 7", "Select hobbies", "Sports hobby selected")
            print("   ⚽ Selecting hobby: Sports")
            self.page.click_element((By.XPATH, "//input[@value='Sports']"))
            print("   ✅ Hobby selected")

            # ===== STEP 8: ENTER ADDRESS =====
            self.log_step("STEP 8", "Enter current address", "Address field populated")
            address = "123 Test Street, Test City"
            print(f"   🏠 Entering address: {address}")
            self.page.type_text((By.ID, "currentAddress"), address)
            print("   ✅ Address entered")

            # ===== STEP 9: SUBMIT FORM =====
            self.log_step(
                "STEP 9", "Submit the form", "Form submitted and modal appears"
            )
            print("   📤 Submitting form...")
            self.page.click_element((By.ID, "submit"))
            print("   ✅ Form submitted")

            # ===== STEP 10: VERIFY SUBMISSION =====
            self.log_step(
                "STEP 10",
                "Verify form submission",
                "Success modal displayed with correct message",
            )
            print("   🔍 Checking for submission modal...")
            assert self.page.is_element_present(
                (By.CLASS_NAME, "modal-content")
            ), "Modal not displayed"
            print("   ✅ Submission modal is present")

            modal_title = self.page.get_text((By.CLASS_NAME, "modal-title"))
            print(f"   📄 Modal title: {modal_title}")
            assert (
                "Thanks for submitting the form" in modal_title
            ), "Incorrect modal title"
            print("   ✅ Form submission verification passed")

            print("\n🎉 DemoQA practice form submission test completed successfully!")

        except Exception as e:
            print(f"\n❌ Test failed: {e}")
            self.log_page_html("demoqa_form_submission")
            raise e

    def testDragDrop(self):
        """
        Test drag and drop functionality on DemoQA
        """
        print("\n" + "=" * 80)
        print("🧪 TEST: DemoQA Drag and Drop Functionality")
        print("=" * 80)

        try:
            # ===== STEP 1: NAVIGATE TO DROPPABLE PAGE =====
            self.log_step(
                "STEP 1", "Navigate to droppable page", "Droppable page loads"
            )
            print("   🌐 Navigating to https://demoqa.com/droppable")
            self.driver.get("https://demoqa.com/droppable")
            print("   ✅ Droppable page loaded")

            # ===== STEP 2: LOCATE DRAGGABLE AND DROPPABLE ELEMENTS =====
            self.log_step(
                "STEP 2", "Locate draggable and droppable elements", "Elements found"
            )
            print("   🔍 Finding draggable element...")
            draggable = self.page.find_element((By.ID, "draggable"))
            print("   ✅ Draggable element found")

            print("   🔍 Finding droppable element...")
            droppable = self.page.find_element((By.ID, "droppable"))
            print("   ✅ Droppable element found")

            # ===== STEP 3: PERFORM DRAG AND DROP =====
            self.log_step(
                "STEP 3",
                "Perform drag and drop operation",
                "Element dragged and dropped",
            )
            print("   🖱️ Performing drag and drop...")
            self.page.drag_and_drop((By.ID, "draggable"), (By.ID, "droppable"))
            print("   ✅ Drag and drop operation completed")

            # ===== STEP 4: VERIFY DROP SUCCESS =====
            self.log_step(
                "STEP 4",
                "Verify drop was successful",
                "Droppable text shows 'Dropped!'",
            )
            print("   🔍 Checking droppable text...")
            droppable_text = self.page.get_text((By.ID, "droppable"))
            print(f"   📄 Droppable text: {droppable_text}")

            assert (
                "Dropped!" in droppable_text
            ), f"Expected 'Dropped!' in text, got: {droppable_text}"
            print("   ✅ Drag and drop verification passed")

            print("\n🎉 DemoQA drag and drop test completed successfully!")

        except Exception as e:
            print(f"\n❌ Test failed: {e}")
            self.log_page_html("demoqa_drag_drop")
            raise e

    def testDynamicProperties(self):
        """
        Test dynamic properties page functionality
        """
        print("\n" + "=" * 80)
        print("🧪 TEST: DemoQA Dynamic Properties")
        print("=" * 80)

        try:
            # ===== STEP 1: NAVIGATE TO DYNAMIC PROPERTIES PAGE =====
            self.log_step(
                "STEP 1",
                "Navigate to dynamic properties page",
                "Dynamic properties page loads",
            )
            print("   🌐 Navigating to https://demoqa.com/dynamic-properties")
            self.driver.get("https://demoqa.com/dynamic-properties")
            print("   ✅ Dynamic properties page loaded")

            # ===== STEP 2: WAIT FOR BUTTON TO BE ENABLED =====
            self.log_step(
                "STEP 2",
                "Wait for button to be enabled",
                "Button becomes clickable after 5 seconds",
            )
            print("   ⏱️ Waiting for button to be enabled (timeout: 10 seconds)...")
            assert self.page.is_element_clickable(
                (By.ID, "enableAfter"), timeout=10
            ), "Button not enabled"
            print("   ✅ Button is now enabled")

            # ===== STEP 3: CLICK THE ENABLED BUTTON =====
            self.log_step(
                "STEP 3", "Click the enabled button", "Button clicked successfully"
            )
            print("   🔘 Clicking the enabled button...")
            self.page.click_element((By.ID, "enableAfter"))
            print("   ✅ Enabled button clicked")

            # ===== STEP 4: VERIFY COLOR CHANGE =====
            self.log_step(
                "STEP 4",
                "Verify color change on color button",
                "Button color has changed",
            )
            print("   🎨 Checking color change on color button...")
            color_button = self.page.find_element((By.ID, "colorChange"))
            color = color_button.value_of_css_property("color")
            print(f"   📊 Button color: {color}")

            assert (
                color != "rgba(255, 255, 255, 1)"
            ), f"Button should not be white, got: {color}"
            print("   ✅ Color change verification passed")

            print("\n🎉 DemoQA dynamic properties test completed successfully!")

        except Exception as e:
            print(f"\n❌ Test failed: {e}")
            self.log_page_html("demoqa_dynamic_properties")
            raise e

    def testAlertsFrames(self):
        """
        Test alerts and frames functionality
        """
        print("\n" + "=" * 80)
        print("🧪 TEST: DemoQA Alerts and Frames")
        print("=" * 80)

        try:
            # ===== STEP 1: NAVIGATE TO ALERTS PAGE =====
            self.log_step(
                "STEP 1", "Navigate to alerts and windows page", "Alerts page loads"
            )
            print("   🌐 Navigating to https://demoqa.com/alertsWindows")
            self.driver.get("https://demoqa.com/alertsWindows")
            print("   ✅ Alerts page loaded")

            # ===== STEP 2: TEST SIMPLE ALERT =====
            self.log_step(
                "STEP 2", "Test simple alert", "Alert appears and is accepted"
            )
            print("   ⚠️ Clicking simple alert button...")
            self.page.click_element((By.ID, "alertButton"))
            print("   ✅ Simple alert triggered")

            print("   ✅ Accepting simple alert...")
            self.page.accept_alert()
            print("   ✅ Simple alert accepted")

            # ===== STEP 3: TEST CONFIRM ALERT =====
            self.log_step(
                "STEP 3", "Test confirm alert", "Confirm alert appears and is accepted"
            )
            print("   ⚠️ Clicking confirm alert button...")
            self.page.click_element((By.ID, "confirmButton"))
            print("   ✅ Confirm alert triggered")

            print("   ✅ Accepting confirm alert...")
            self.page.accept_alert()
            print("   ✅ Confirm alert accepted")

            # ===== STEP 4: TEST PROMPT ALERT =====
            self.log_step(
                "STEP 4",
                "Test prompt alert",
                "Prompt alert appears, text entered, and accepted",
            )
            print("   ⚠️ Clicking prompt alert button...")
            self.page.click_element((By.ID, "promtButton"))
            print("   ✅ Prompt alert triggered")

            alert = self.driver.switch_to.alert
            print("   📝 Entering text in prompt: Test Name")
            alert.send_keys("Test Name")
            print("   ✅ Text entered in prompt")

            print("   ✅ Accepting prompt alert...")
            alert.accept()
            print("   ✅ Prompt alert accepted")

            print("\n🎉 DemoQA alerts and frames test completed successfully!")

        except Exception as e:
            print(f"\n❌ Test failed: {e}")
            self.log_page_html("demoqa_alerts_frames")
            raise e

    def testBookStore(self):
        """
        Test book store application functionality
        """
        print("\n" + "=" * 80)
        print("🧪 TEST: DemoQA Book Store Application")
        print("=" * 80)

        try:
            # ===== STEP 1: NAVIGATE TO BOOK STORE =====
            self.log_step("STEP 1", "Navigate to book store", "Book store page loads")
            print("   🌐 Navigating to https://demoqa.com/books")
            self.driver.get("https://demoqa.com/books")
            print("   ✅ Book store page loaded")

            # ===== STEP 2: SEARCH FOR BOOKS =====
            self.log_step("STEP 2", "Search for books", "Search results displayed")
            search_term = "Git"
            print(f"   🔍 Searching for books: {search_term}")
            self.page.type_text((By.ID, "searchBox"), search_term)
            print("   ✅ Search performed")

            # ===== STEP 3: VERIFY SEARCH RESULTS =====
            self.log_step(
                "STEP 3", "Verify search results", "Books found in search results"
            )
            print("   📚 Checking search results...")
            books = self.page.find_elements((By.CLASS_NAME, "rt-tr-group"))
            print(f"   📊 Number of books found: {len(books)}")

            assert len(books) > 0, "No books found in search results"
            print("   ✅ Search results verified")

            # ===== STEP 4: CLICK ON FIRST BOOK =====
            self.log_step("STEP 4", "Click on first book", "Book details page loads")
            print("   📖 Clicking on first book...")
            if books:
                self.page.click_element((By.CLASS_NAME, "rt-tr-group"))
                print("   ✅ First book clicked")

                # ===== STEP 5: VERIFY BOOK DETAILS PAGE =====
                self.log_step(
                    "STEP 5", "Verify book details page", "Book details page displayed"
                )
                print("   🔍 Checking book details page...")
                assert self.page.is_element_present(
                    (By.CLASS_NAME, "profile-wrapper")
                ), "Book details page not loaded"
                print("   ✅ Book details page verified")
            else:
                print("   ⚠️ No books available to click")

            print("\n🎉 DemoQA book store test completed successfully!")

        except Exception as e:
            print(f"\n❌ Test failed: {e}")
            self.log_page_html("demoqa_book_store")
            raise e

    def testWidgets(self):
        """
        Test widgets interaction functionality
        """
        print("\n" + "=" * 80)
        print("🧪 TEST: DemoQA Widgets Interaction")
        print("=" * 80)

        try:
            # ===== STEP 1: NAVIGATE TO WIDGETS PAGE =====
            self.log_step("STEP 1", "Navigate to widgets page", "Widgets page loads")
            print("   🌐 Navigating to https://demoqa.com/widgets")
            self.driver.get("https://demoqa.com/widgets")
            print("   ✅ Widgets page loaded")

            # ===== STEP 2: TEST ACCORDION =====
            self.log_step(
                "STEP 2", "Test accordion functionality", "Accordion section expands"
            )
            print("   📋 Clicking accordion section...")
            self.page.click_element((By.ID, "section1Heading"))
            print("   ✅ Accordion section clicked")

            print("   🔍 Checking accordion content visibility...")
            assert self.page.is_element_visible(
                (By.ID, "section1Content")
            ), "Accordion content not visible"
            print("   ✅ Accordion content is visible")

            # ===== STEP 3: TEST TABS =====
            self.log_step("STEP 3", "Test tabs functionality", "Tab content switches")
            print("   📑 Clicking 'What' tab...")
            self.page.click_element((By.ID, "demo-tab-what"))
            print("   ✅ 'What' tab clicked")

            print("   🔍 Checking tab content visibility...")
            assert self.page.is_element_visible(
                (By.ID, "demo-tabpane-what")
            ), "Tab content not visible"
            print("   ✅ Tab content is visible")

            # ===== STEP 4: TEST TOOLTIPS =====
            self.log_step(
                "STEP 4", "Test tooltip functionality", "Tooltip appears on hover"
            )
            print("   💡 Hovering over tooltip button...")
            self.page.hover_over_element((By.ID, "toolTipButton"))
            print("   ✅ Hover action performed")

            print("   🔍 Checking tooltip presence...")
            assert self.page.is_element_present(
                (By.CLASS_NAME, "tooltip-inner")
            ), "Tooltip not present"
            print("   ✅ Tooltip is present")

            print("\n🎉 DemoQA widgets test completed successfully!")

        except Exception as e:
            print(f"\n❌ Test failed: {e}")
            self.log_page_html("demoqa_widgets")
            raise e

    @pytest.mark.slow
    def testProgressBar(self):
        """
        Test progress bar functionality
        """
        print("\n" + "=" * 80)
        print("🧪 TEST: DemoQA Progress Bar")
        print("=" * 80)

        try:
            # ===== STEP 1: NAVIGATE TO PROGRESS BAR PAGE =====
            self.log_step(
                "STEP 1", "Navigate to progress bar page", "Progress bar page loads"
            )
            print("   🌐 Navigating to https://demoqa.com/progress-bar")
            self.driver.get("https://demoqa.com/progress-bar")
            print("   ✅ Progress bar page loaded")

            # ===== STEP 2: START PROGRESS BAR =====
            self.log_step("STEP 2", "Start progress bar", "Progress bar begins filling")
            print("   ▶️ Starting progress bar...")
            self.page.click_element((By.ID, "startStopButton"))
            print("   ✅ Progress bar started")

            # ===== STEP 3: WAIT FOR PROGRESS COMPLETION =====
            self.log_step(
                "STEP 3", "Wait for progress completion", "Progress bar reaches 100%"
            )
            print("   ⏱️ Waiting for progress to complete (timeout: 30 seconds)...")
            self.page.wait_for_element_to_disappear(
                (By.CLASS_NAME, "progress-bar"), timeout=30
            )
            print("   ✅ Progress bar completed")

            # ===== STEP 4: VERIFY COMPLETION =====
            self.log_step("STEP 4", "Verify progress completion", "Progress shows 100%")
            print("   🔍 Checking progress completion...")
            progress_text = self.page.get_text((By.CLASS_NAME, "progress-bar"))
            print(f"   📊 Progress text: {progress_text}")

            assert (
                "100%" in progress_text
            ), f"Progress should be 100%, got: {progress_text}"
            print("   ✅ Progress completion verified")

            print("\n🎉 DemoQA progress bar test completed successfully!")

        except Exception as e:
            print(f"\n❌ Test failed: {e}")
            self.log_page_html("demoqa_progress_bar")
            raise e

    @pytest.mark.critical
    def testCriticalFlow(self):
        """
        Critical user flow test for DemoQA
        """
        print("\n" + "=" * 80)
        print("🧪 TEST: DemoQA Critical User Flow")
        print("=" * 80)

        try:
            # ===== STEP 1: NAVIGATE TO MAIN PAGE =====
            self.log_step(
                "STEP 1",
                "Navigate to DemoQA main page",
                "Main page loads with ToolsQA title",
            )
            print("   🌐 Navigating to https://demoqa.com/")
            self.driver.get("https://demoqa.com/")
            print("   ✅ Main page loaded")

            # ===== STEP 2: VERIFY PAGE LOADS =====
            self.log_step(
                "STEP 2",
                "Verify main page loads correctly",
                "Page title contains ToolsQA",
            )
            print("   🔍 Checking page title...")
            page_title = self.page.get_page_title()
            print(f"   📄 Page title: {page_title}")

            assert (
                "ToolsQA" in page_title
            ), f"Expected 'ToolsQA' in title, got: {page_title}"
            print("   ✅ Main page verification passed")

            # ===== STEP 3: NAVIGATE TO ELEMENTS =====
            self.log_step(
                "STEP 3", "Navigate to elements section", "Elements page loads"
            )
            print("   🔗 Clicking on Elements card...")
            self.page.click_element(
                (
                    By.XPATH,
                    "//div[contains(@class, 'card-body') and contains(text(), 'Elements')]",
                )
            )
            print("   ✅ Elements card clicked")

            # ===== STEP 4: VERIFY ELEMENTS PAGE =====
            self.log_step(
                "STEP 4",
                "Verify elements page loads",
                "Elements page title contains 'Elements'",
            )
            print("   🔍 Checking elements page title...")
            elements_title = self.page.get_page_title()
            print(f"   📄 Elements page title: {elements_title}")

            assert (
                "Elements" in elements_title
            ), f"Expected 'Elements' in title, got: {elements_title}"
            print("   ✅ Elements page verification passed")

            # ===== STEP 5: TEST TEXT BOX =====
            self.log_step(
                "STEP 5",
                "Test text box functionality",
                "Text box form submitted successfully",
            )
            print("   📝 Clicking on Text Box...")
            self.page.click_element((By.XPATH, "//span[text()='Text Box']"))
            print("   ✅ Text Box clicked")

            print("   👤 Entering user name: Test User")
            self.page.type_text((By.ID, "userName"), "Test User")

            print("   📧 Entering user email: test@example.com")
            self.page.type_text((By.ID, "userEmail"), "test@example.com")

            print("   📤 Submitting text box form...")
            self.page.click_element((By.ID, "submit"))
            print("   ✅ Text box form submitted")

            # ===== STEP 6: VERIFY SUBMISSION =====
            self.log_step(
                "STEP 6", "Verify text box submission", "Output element is present"
            )
            print("   🔍 Checking for output element...")
            assert self.page.is_element_present(
                (By.ID, "output")
            ), "Output element not present"
            print("   ✅ Text box submission verified")

            print("\n🎉 DemoQA critical user flow test completed successfully!")

        except Exception as e:
            print(f"\n❌ Test failed: {e}")
            self.log_page_html("demoqa_critical_flow")
            raise e
