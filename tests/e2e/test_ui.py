"""
Comprehensive UI tests using Page Object Model for practice sites.
"""
import pytest
import os
import time
from pages.demoqa_pages import *
from pages.the_internet_pages import *

class TestUI:
    @pytest.fixture(autouse=True)
    def setup_pages(self, driver):
        """Setup page objects for UI testing."""
        print("\n🔧 Setting up page objects for UI testing...")
        self.driver = driver
        self.demoqa_main = DemoQAMainPage(driver)
        self.the_internet_main = TheInternetMainPage(driver)
        print("✅ Page objects initialized successfully")

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

    def log_step(self, step_name, description, expected_result=None):
        """Log test step details to console."""
        print(f"\n📋 {step_name}")
        print(f"   Description: {description}")
        if expected_result:
            print(f"   Expected: {expected_result}")

    def testDemoqaForm(self):
        """
        Test DemoQA form submission workflow
        """
        print("\n" + "="*80)
        print("🧪 TEST: DemoQA Form Submission Workflow")
        print("="*80)
        
        try:
            # ===== STEP 1: NAVIGATE TO DEMOQA =====
            self.log_step("STEP 1", "Navigate to DemoQA homepage", "Page loads with DEMOQA title")
            print("   🌐 Navigating to https://demoqa.com/")
            self.driver.get("https://demoqa.com/")
            
            # Validate page title
            page_title = self.demoqa_main.get_page_title()
            print(f"   📄 Page title: {page_title}")
            assert "DEMOQA" in page_title, f"Expected 'DEMOQA' in title, got: {page_title}"
            print("   ✅ DemoQA homepage loaded successfully")
            
            # ===== STEP 2: NAVIGATE TO ELEMENTS =====
            self.log_step("STEP 2", "Navigate to Elements section", "Elements page loads")
            print("   🔗 Clicking on Elements card...")
            elements_page = self.demoqa_main.navigate_to_elements()
            print("   ✅ Elements page loaded")
            
            # ===== STEP 3: OPEN TEXT BOX =====
            self.log_step("STEP 3", "Open Text Box form", "Text Box form page loads")
            print("   📝 Clicking on Text Box...")
            text_box_page = elements_page.click_text_box()
            print("   ✅ Text Box form page loaded")
            
            # ===== STEP 4: FILL FORM DATA =====
            self.log_step("STEP 4", "Fill form with test data", "Form fields populated")
            form_data = {
                "full_name": "John Doe",
                "email": "john.doe@example.com",
                "current_address": "123 Current Street",
                "permanent_address": "456 Permanent Street"
            }
            print(f"   📝 Filling form with data: {form_data}")
            
            text_box_page.fill_form(
                full_name=form_data["full_name"],
                email=form_data["email"],
                current_address=form_data["current_address"],
                permanent_address=form_data["permanent_address"]
            )
            print("   ✅ Form filled successfully")
            
            # ===== STEP 5: SUBMIT FORM =====
            self.log_step("STEP 5", "Submit the form", "Form submitted and output displayed")
            print("   📤 Submitting form...")
            text_box_page.submit_form()
            print("   ✅ Form submitted")
            
            # ===== STEP 6: VALIDATE OUTPUT =====
            self.log_step("STEP 6", "Validate form output", "Output contains submitted data")
            print("   🔍 Checking for output display...")
            assert text_box_page.is_output_present(), "Form output not displayed"
            print("   ✅ Output is present")
            
            output_text = text_box_page.get_output_text()
            print(f"   📄 Output text: {output_text}")
            
            # Validate output contains submitted data
            assert "John Doe" in output_text, "Full name not found in output"
            assert "john.doe@example.com" in output_text, "Email not found in output"
            print("   ✅ Output validation passed")
            
            print("\n🎉 DemoQA form submission test completed successfully!")
            
        except Exception as e:
            print(f"\n❌ Test failed: {e}")
            self.log_page_html("demoqa_textbox_form")
            raise e

    def testDemoqaDragDrop(self):
        """
        Test DemoQA drag and drop functionality
        """
        print("\n" + "="*80)
        print("🧪 TEST: DemoQA Drag and Drop Functionality")
        print("="*80)
        
        try:
            # ===== STEP 1: NAVIGATE TO DEMOQA =====
            self.log_step("STEP 1", "Navigate to DemoQA homepage", "Page loads with DEMOQA title")
            print("   🌐 Navigating to https://demoqa.com/")
            self.driver.get("https://demoqa.com/")
            print("   ✅ DemoQA homepage loaded")
            
            # ===== STEP 2: NAVIGATE TO INTERACTIONS =====
            self.log_step("STEP 2", "Navigate to Interactions section", "Interactions page loads")
            print("   🔗 Clicking on Interactions card...")
            interactions_page = self.demoqa_main.navigate_to_interactions()
            print("   ✅ Interactions page loaded")
            
            # ===== STEP 3: OPEN DROPPABLE =====
            self.log_step("STEP 3", "Open Droppable section", "Droppable page loads")
            print("   🎯 Clicking on Droppable...")
            droppable_page = interactions_page.click_droppable()
            print("   ✅ Droppable page loaded")
            
            # ===== STEP 4: PERFORM DRAG AND DROP =====
            self.log_step("STEP 4", "Perform drag and drop operation", "Element dragged and dropped")
            print("   🖱️ Performing drag and drop...")
            droppable_page.perform_drag_and_drop()
            print("   ✅ Drag and drop operation completed")
            
            # ===== STEP 5: VALIDATE RESULT =====
            self.log_step("STEP 5", "Validate drop result", "Droppable text shows 'Dropped!'")
            print("   🔍 Checking droppable text...")
            droppable_text = droppable_page.get_droppable_text()
            print(f"   📄 Droppable text: {droppable_text}")
            
            assert "Dropped!" in droppable_text, f"Expected 'Dropped!' in text, got: {droppable_text}"
            print("   ✅ Drag and drop validation passed")
            
            print("\n🎉 DemoQA drag and drop test completed successfully!")
            
        except Exception as e:
            print(f"\n❌ Test failed: {e}")
            self.log_page_html("demoqa_drag_drop")
            raise e

    def testInternetLogin(self):
        """
        Test The Internet login and logout functionality
        """
        print("\n" + "="*80)
        print("🧪 TEST: The Internet Login and Logout Functionality")
        print("="*80)
        
        try:
            # ===== STEP 1: NAVIGATE TO THE INTERNET =====
            self.log_step("STEP 1", "Navigate to The Internet homepage", "Page loads with 'The Internet' title")
            print("   🌐 Navigating to https://the-internet.herokuapp.com/")
            self.driver.get("https://the-internet.herokuapp.com/")
            
            page_title = self.the_internet_main.get_page_title()
            print(f"   📄 Page title: {page_title}")
            assert "The Internet" in page_title, f"Expected 'The Internet' in title, got: {page_title}"
            print("   ✅ The Internet homepage loaded successfully")
            
            # ===== STEP 2: NAVIGATE TO LOGIN =====
            self.log_step("STEP 2", "Navigate to Form Authentication", "Login page loads")
            print("   🔐 Clicking on Form Authentication...")
            login_page = self.the_internet_main.click_form_authentication()
            print("   ✅ Login page loaded")
            
            # ===== STEP 3: PERFORM LOGIN =====
            self.log_step("STEP 3", "Perform login with valid credentials", "User logged in successfully")
            credentials = {
                "username": "tomsmith",
                "password": "SuperSecretPassword!"
            }
            print(f"   🔑 Logging in with credentials: {credentials}")
            
            login_page.login(credentials["username"], credentials["password"])
            print("   ✅ Login attempt completed")
            
            # ===== STEP 4: VALIDATE LOGIN SUCCESS =====
            self.log_step("STEP 4", "Validate successful login", "User is logged in")
            print("   🔍 Checking login status...")
            assert login_page.is_logged_in(), "User should be logged in"
            print("   ✅ Login successful")
            
            # ===== STEP 5: PERFORM LOGOUT =====
            self.log_step("STEP 5", "Perform logout", "User logged out successfully")
            print("   🚪 Logging out...")
            login_page.logout()
            print("   ✅ Logout completed")
            
            # ===== STEP 6: VALIDATE LOGOUT SUCCESS =====
            self.log_step("STEP 6", "Validate successful logout", "User is logged out")
            print("   🔍 Checking logout status...")
            assert not login_page.is_logged_in(), "User should be logged out"
            print("   ✅ Logout successful")
            
            print("\n🎉 The Internet login/logout test completed successfully!")
            
        except Exception as e:
            print(f"\n❌ Test failed: {e}")
            self.log_page_html("internet_login_logout")
            raise e

    def testInternetCheckboxes(self):
        """
        Test The Internet checkboxes functionality
        """
        print("\n" + "="*80)
        print("🧪 TEST: The Internet Checkboxes Functionality")
        print("="*80)
        
        try:
            # ===== STEP 1: NAVIGATE TO THE INTERNET =====
            self.log_step("STEP 1", "Navigate to The Internet homepage", "Page loads")
            print("   🌐 Navigating to https://the-internet.herokuapp.com/")
            self.driver.get("https://the-internet.herokuapp.com/")
            print("   ✅ The Internet homepage loaded")
            
            # ===== STEP 2: NAVIGATE TO CHECKBOXES =====
            self.log_step("STEP 2", "Navigate to Checkboxes page", "Checkboxes page loads")
            print("   ☑️ Clicking on Checkboxes...")
            checkboxes_page = self.the_internet_main.click_checkboxes()
            print("   ✅ Checkboxes page loaded")
            
            # ===== STEP 3: CHECK ALL CHECKBOXES =====
            self.log_step("STEP 3", "Check all checkboxes", "All checkboxes become checked")
            print("   ☑️ Checking all checkboxes...")
            checkboxes_page.check_all_checkboxes()
            print("   ✅ All checkboxes checked")
            
            # ===== STEP 4: VALIDATE CHECKED STATE =====
            self.log_step("STEP 4", "Validate checkboxes are checked", "Both checkboxes are checked")
            print("   🔍 Validating checkbox 1 is checked...")
            assert checkboxes_page.is_checkbox_1_checked(), "Checkbox 1 should be checked"
            print("   ✅ Checkbox 1 is checked")
            
            print("   🔍 Validating checkbox 2 is checked...")
            assert checkboxes_page.is_checkbox_2_checked(), "Checkbox 2 should be checked"
            print("   ✅ Checkbox 2 is checked")
            
            # ===== STEP 5: UNCHECK ALL CHECKBOXES =====
            self.log_step("STEP 5", "Uncheck all checkboxes", "All checkboxes become unchecked")
            print("   ☐ Unchecking all checkboxes...")
            checkboxes_page.uncheck_all_checkboxes()
            print("   ✅ All checkboxes unchecked")
            
            # ===== STEP 6: VALIDATE UNCHECKED STATE =====
            self.log_step("STEP 6", "Validate checkboxes are unchecked", "Both checkboxes are unchecked")
            print("   🔍 Validating checkbox 1 is unchecked...")
            assert not checkboxes_page.is_checkbox_1_checked(), "Checkbox 1 should be unchecked"
            print("   ✅ Checkbox 1 is unchecked")
            
            print("   🔍 Validating checkbox 2 is unchecked...")
            assert not checkboxes_page.is_checkbox_2_checked(), "Checkbox 2 should be unchecked"
            print("   ✅ Checkbox 2 is unchecked")
            
            print("\n🎉 The Internet checkboxes test completed successfully!")
            
        except Exception as e:
            print(f"\n❌ Test failed: {e}")
            self.log_page_html("internet_checkboxes")
            raise e

    def testInternetAlert(self):
        """
        Test The Internet JavaScript alerts functionality
        """
        print("\n" + "="*80)
        print("🧪 TEST: The Internet JavaScript Alerts Functionality")
        print("="*80)
        
        try:
            # ===== STEP 1: NAVIGATE TO THE INTERNET =====
            self.log_step("STEP 1", "Navigate to The Internet homepage", "Page loads")
            print("   🌐 Navigating to https://the-internet.herokuapp.com/")
            self.driver.get("https://the-internet.herokuapp.com/")
            print("   ✅ The Internet homepage loaded")
            
            # ===== STEP 2: NAVIGATE TO JAVASCRIPT ALERTS =====
            self.log_step("STEP 2", "Navigate to JavaScript Alerts", "Alerts page loads")
            print("   ⚠️ Clicking on JavaScript Alerts...")
            alerts_page = self.the_internet_main.click_javascript_alerts()
            print("   ✅ JavaScript Alerts page loaded")
            
            # ===== STEP 3: TRIGGER JS ALERT =====
            self.log_step("STEP 3", "Click JS Alert button", "JavaScript alert appears")
            print("   🔘 Clicking JS Alert button...")
            alerts_page.click_js_alert()
            print("   ✅ JS Alert triggered")
            
            # ===== STEP 4: ACCEPT ALERT =====
            self.log_step("STEP 4", "Accept the alert", "Alert accepted and result displayed")
            print("   ✅ Accepting alert...")
            alerts_page.accept_alert()
            print("   ✅ Alert accepted")
            
            # ===== STEP 5: VALIDATE RESULT =====
            self.log_step("STEP 5", "Validate alert result", "Result text shows success message")
            print("   🔍 Checking result text...")
            result_text = alerts_page.get_result_text()
            print(f"   📄 Result text: {result_text}")
            
            expected_text = "You successfully clicked an alert"
            assert expected_text in result_text, f"Expected '{expected_text}' in result, got: {result_text}"
            print("   ✅ Alert result validation passed")
            
            print("\n🎉 The Internet JavaScript alerts test completed successfully!")
            
        except Exception as e:
            print(f"\n❌ Test failed: {e}")
            self.log_page_html("internet_js_alert")
            raise e 