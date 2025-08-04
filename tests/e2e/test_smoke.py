"""
Smoke tests for E2E testing - quick tests to verify basic functionality.
"""

import pytest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.logger import logger


class TestSmoke:
    """Smoke tests for basic E2E functionality."""

    def setup_method(self):
        """Set up test method."""
        logger.info("Setting up smoke test...")

    def teardown_method(self):
        """Tear down test method."""
        logger.info("Tearing down smoke test...")

    def testBasicPageLoad(self, driver):
        """Test basic page loading functionality."""
        logger.info("🧪 SMOKE TEST: Basic Page Load")
        
        page = BasePage(driver)
        
        # Test 1: Navigate to a simple page
        print("   🌐 Testing navigation to Google...")
        driver.get("https://www.google.com")
        
        # Test 2: Verify page loaded
        print("   🔍 Checking page title...")
        title = driver.title
        print(f"   📄 Page title: {title}")
        assert "Google" in title, f"Expected Google in title, got: {title}"
        
        # Test 3: Find a basic element
        print("   🔍 Looking for search box...")
        search_box = page.find_element((By.NAME, "q"), timeout=10)
        assert search_box is not None, "Search box not found"
        
        # Test 4: Test auto-click outside (should be conservative in CI)
        print("   🎯 Testing auto-click outside functionality...")
        if page.ci_mode:
            print("   ℹ️ Running in CI mode - using conservative auto-click")
        else:
            print("   ℹ️ Running in local mode - using full auto-click")
            
        page.dismiss_overlays()  # Should work without hanging
        
        print("   ✅ Basic smoke test completed successfully!")
        logger.info("✅ Smoke test passed")

    def testSimpleInteraction(self, driver):
        """Test simple interaction without complex forms."""
        logger.info("🧪 SMOKE TEST: Simple Interaction")
        
        page = BasePage(driver)
        
        # Test simple interaction on a reliable site
        print("   🌐 Testing simple interaction...")
        driver.get("https://example.com")
        
        # Verify page loads
        title = driver.title
        print(f"   📄 Page title: {title}")
        assert "Example" in title, f"Expected Example in title, got: {title}"
        
        # Test element presence
        print("   🔍 Checking for page content...")
        content = page.find_element((By.TAG_NAME, "h1"), timeout=5)
        assert content is not None, "Page content not found"
        
        print("   ✅ Simple interaction test completed successfully!")
        logger.info("✅ Simple interaction test passed")