"""
Unit tests for calculator functionality.
"""
import pytest
from utils.calculator import Calculator


class TestCalculator:
    """Test cases for Calculator class."""
    
    def setup_method(self):
        """Setup method called before each test."""
        print("\n🔧 Setting up Calculator instance...")
        self.calc = Calculator()
        print("✅ Calculator instance created successfully")
    
    def log_test_step(self, step_name, description, input_data=None, expected_result=None):
        """Log test step details to console."""
        print(f"\n📋 {step_name}")
        print(f"   Description: {description}")
        if input_data:
            print(f"   Input: {input_data}")
        if expected_result:
            print(f"   Expected: {expected_result}")
    
    def testAdd(self):
        """
        Test addition operation with detailed logging
        """
        print("\n" + "="*80)
        print("🧪 TEST: Calculator Addition Operation")
        print("="*80)
        
        # ===== STEP 1: PERFORM ADDITION =====
        self.log_test_step("STEP 1", "Perform addition operation", "2 + 3", "5")
        print("   ➕ Calculating: 2 + 3")
        result = self.calc.add(2, 3)
        print(f"   📊 Result: {result}")
        
        # ===== STEP 2: VALIDATE RESULT =====
        self.log_test_step("STEP 2", "Validate addition result", None, "Result should equal 5")
        assert result == 5, f"Expected 5, got {result}"
        print("   ✅ Addition test passed")
        
        print("\n🎉 Calculator addition test completed successfully!")
    
    def testSubtract(self):
        """
        Test subtraction operation with detailed logging
        """
        print("\n" + "="*80)
        print("🧪 TEST: Calculator Subtraction Operation")
        print("="*80)
        
        # ===== STEP 1: PERFORM SUBTRACTION =====
        self.log_test_step("STEP 1", "Perform subtraction operation", "5 - 3", "2")
        print("   ➖ Calculating: 5 - 3")
        result = self.calc.subtract(5, 3)
        print(f"   📊 Result: {result}")
        
        # ===== STEP 2: VALIDATE RESULT =====
        self.log_test_step("STEP 2", "Validate subtraction result", None, "Result should equal 2")
        assert result == 2, f"Expected 2, got {result}"
        print("   ✅ Subtraction test passed")
        
        print("\n🎉 Calculator subtraction test completed successfully!")
    
    def testMultiply(self):
        """
        Test multiplication operation with detailed logging
        """
        print("\n" + "="*80)
        print("🧪 TEST: Calculator Multiplication Operation")
        print("="*80)
        
        # ===== STEP 1: PERFORM MULTIPLICATION =====
        self.log_test_step("STEP 1", "Perform multiplication operation", "4 * 3", "12")
        print("   ✖️ Calculating: 4 * 3")
        result = self.calc.multiply(4, 3)
        print(f"   📊 Result: {result}")
        
        # ===== STEP 2: VALIDATE RESULT =====
        self.log_test_step("STEP 2", "Validate multiplication result", None, "Result should equal 12")
        assert result == 12, f"Expected 12, got {result}"
        print("   ✅ Multiplication test passed")
        
        print("\n🎉 Calculator multiplication test completed successfully!")
    
    def testDivide(self):
        """
        Test division operation with detailed logging
        """
        print("\n" + "="*80)
        print("🧪 TEST: Calculator Division Operation")
        print("="*80)
        
        # ===== STEP 1: PERFORM DIVISION =====
        self.log_test_step("STEP 1", "Perform division operation", "10 / 2", "5")
        print("   ➗ Calculating: 10 / 2")
        result = self.calc.divide(10, 2)
        print(f"   📊 Result: {result}")
        
        # ===== STEP 2: VALIDATE RESULT =====
        self.log_test_step("STEP 2", "Validate division result", None, "Result should equal 5")
        assert result == 5, f"Expected 5, got {result}"
        print("   ✅ Division test passed")
        
        print("\n🎉 Calculator division test completed successfully!")
    
    def testDivideByZero(self):
        """
        Test division by zero exception handling
        """
        print("\n" + "="*80)
        print("🧪 TEST: Calculator Division by Zero Exception")
        print("="*80)
        
        # ===== STEP 1: ATTEMPT DIVISION BY ZERO =====
        self.log_test_step("STEP 1", "Attempt division by zero", "10 / 0", "ValueError exception")
        print("   ⚠️ Attempting: 10 / 0")
        
        # ===== STEP 2: VALIDATE EXCEPTION =====
        self.log_test_step("STEP 2", "Validate exception is raised", None, "ValueError with specific message")
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)
        print("   ✅ Division by zero exception handled correctly")
        
        print("\n🎉 Calculator division by zero test completed successfully!")
    
    def testPower(self):
        """
        Test power operation with detailed logging
        """
        print("\n" + "="*80)
        print("🧪 TEST: Calculator Power Operation")
        print("="*80)
        
        # ===== STEP 1: PERFORM POWER OPERATION =====
        self.log_test_step("STEP 1", "Perform power operation", "2 ^ 3", "8")
        print("   🔢 Calculating: 2 ^ 3")
        result = self.calc.power(2, 3)
        print(f"   📊 Result: {result}")
        
        # ===== STEP 2: VALIDATE RESULT =====
        self.log_test_step("STEP 2", "Validate power result", None, "Result should equal 8")
        assert result == 8, f"Expected 8, got {result}"
        print("   ✅ Power test passed")
        
        print("\n🎉 Calculator power test completed successfully!")
    
    def testSqrt(self):
        """
        Test square root operation with detailed logging
        """
        print("\n" + "="*80)
        print("🧪 TEST: Calculator Square Root Operation")
        print("="*80)
        
        # ===== STEP 1: PERFORM SQUARE ROOT =====
        self.log_test_step("STEP 1", "Perform square root operation", "√16", "4")
        print("   √ Calculating: √16")
        result = self.calc.sqrt(16)
        print(f"   📊 Result: {result}")
        
        # ===== STEP 2: VALIDATE RESULT =====
        self.log_test_step("STEP 2", "Validate square root result", None, "Result should equal 4")
        assert result == 4, f"Expected 4, got {result}"
        print("   ✅ Square root test passed")
        
        print("\n🎉 Calculator square root test completed successfully!")
    
    def testSqrtNegative(self):
        """
        Test square root of negative number exception handling
        """
        print("\n" + "="*80)
        print("🧪 TEST: Calculator Square Root of Negative Number")
        print("="*80)
        
        # ===== STEP 1: ATTEMPT SQUARE ROOT OF NEGATIVE =====
        self.log_test_step("STEP 1", "Attempt square root of negative number", "√(-1)", "ValueError exception")
        print("   ⚠️ Attempting: √(-1)")
        
        # ===== STEP 2: VALIDATE EXCEPTION =====
        self.log_test_step("STEP 2", "Validate exception is raised", None, "ValueError with specific message")
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calc.sqrt(-1)
        print("   ✅ Square root of negative number exception handled correctly")
        
        print("\n🎉 Calculator square root of negative number test completed successfully!")
    
    @pytest.mark.parametrize("a, b, expected", [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (100, 200, 300),
    ])
    def testAddParametrized(self, a, b, expected):
        """
        Test addition with multiple values using parametrization
        """
        print(f"\n🧪 TEST: Calculator Addition Parametrized ({a} + {b} = {expected})")
        
        # ===== STEP 1: PERFORM PARAMETRIZED ADDITION =====
        self.log_test_step("STEP 1", f"Perform addition: {a} + {b}", f"{a} + {b}", expected)
        print(f"   ➕ Calculating: {a} + {b}")
        result = self.calc.add(a, b)
        print(f"   📊 Result: {result}")
        
        # ===== STEP 2: VALIDATE PARAMETRIZED RESULT =====
        self.log_test_step("STEP 2", "Validate parametrized result", None, f"Result should equal {expected}")
        assert result == expected, f"Expected {expected}, got {result}"
        print(f"   ✅ Parametrized addition test passed: {a} + {b} = {result}")
    
    @pytest.mark.parametrize("a, b, expected", [
        (5, 3, 2),
        (0, 0, 0),
        (1, 1, 0),
        (100, 50, 50),
    ])
    def testSubtractParametrized(self, a, b, expected):
        """
        Test subtraction with multiple values using parametrization
        """
        print(f"\n🧪 TEST: Calculator Subtraction Parametrized ({a} - {b} = {expected})")
        
        # ===== STEP 1: PERFORM PARAMETRIZED SUBTRACTION =====
        self.log_test_step("STEP 1", f"Perform subtraction: {a} - {b}", f"{a} - {b}", expected)
        print(f"   ➖ Calculating: {a} - {b}")
        result = self.calc.subtract(a, b)
        print(f"   📊 Result: {result}")
        
        # ===== STEP 2: VALIDATE PARAMETRIZED RESULT =====
        self.log_test_step("STEP 2", "Validate parametrized result", None, f"Result should equal {expected}")
        assert result == expected, f"Expected {expected}, got {result}"
        print(f"   ✅ Parametrized subtraction test passed: {a} - {b} = {result}")
    
    def testHistory(self):
        """
        Test calculator history functionality with detailed logging
        """
        print("\n" + "="*80)
        print("🧪 TEST: Calculator History Functionality")
        print("="*80)
        
        # ===== STEP 1: PERFORM MULTIPLE OPERATIONS =====
        self.log_test_step("STEP 1", "Perform multiple operations to build history", "2+3, 5-2, 3*4", "History with 3 entries")
        print("   📝 Performing operations to build history...")
        
        print("   ➕ Operation 1: 2 + 3")
        self.calc.add(2, 3)
        
        print("   ➖ Operation 2: 5 - 2")
        self.calc.subtract(5, 2)
        
        print("   ✖️ Operation 3: 3 * 4")
        self.calc.multiply(3, 4)
        
        # ===== STEP 2: RETRIEVE HISTORY =====
        self.log_test_step("STEP 2", "Retrieve calculator history", None, "History should contain 3 entries")
        print("   📋 Retrieving calculator history...")
        history = self.calc.get_history()
        print(f"   📄 History entries: {history}")
        
        # ===== STEP 3: VALIDATE HISTORY =====
        self.log_test_step("STEP 3", "Validate history entries", None, "Correct history entries")
        print("   🔍 Validating history entries...")
        
        assert len(history) == 3, f"Expected 3 history entries, got {len(history)}"
        print("   ✅ History length is correct")
        
        assert history[0] == "2 + 3 = 5", f"Expected '2 + 3 = 5', got '{history[0]}'"
        assert history[1] == "5 - 2 = 3", f"Expected '5 - 2 = 3', got '{history[1]}'"
        assert history[2] == "3 * 4 = 12", f"Expected '3 * 4 = 12', got '{history[2]}'"
        print("   ✅ All history entries are correct")
        
        print("\n🎉 Calculator history test completed successfully!")
    
    def testClearHistory(self):
        """
        Test clearing calculator history with detailed logging
        """
        print("\n" + "="*80)
        print("🧪 TEST: Calculator Clear History Functionality")
        print("="*80)
        
        # ===== STEP 1: ADD OPERATION TO HISTORY =====
        self.log_test_step("STEP 1", "Add operation to history", "2 + 3", "History with 1 entry")
        print("   ➕ Adding operation to history: 2 + 3")
        self.calc.add(2, 3)
        
        # ===== STEP 2: CLEAR HISTORY =====
        self.log_test_step("STEP 2", "Clear calculator history", None, "History should be empty")
        print("   🗑️ Clearing calculator history...")
        self.calc.clear_history()
        
        # ===== STEP 3: VALIDATE CLEARED HISTORY =====
        self.log_test_step("STEP 3", "Validate history is cleared", None, "History should have 0 entries")
        print("   🔍 Validating history is cleared...")
        history = self.calc.get_history()
        print(f"   📄 History after clearing: {history}")
        
        assert len(history) == 0, f"Expected 0 history entries, got {len(history)}"
        print("   ✅ History cleared successfully")
        
        print("\n🎉 Calculator clear history test completed successfully!")
    
    @pytest.mark.slow
    def testLargeNumbers(self):
        """
        Test operations with large numbers with detailed logging
        """
        print("\n" + "="*80)
        print("🧪 TEST: Calculator Large Numbers Operation")
        print("="*80)
        
        # ===== STEP 1: PERFORM OPERATION WITH LARGE NUMBERS =====
        large_num = 999999999
        self.log_test_step("STEP 1", "Perform addition with large numbers", f"{large_num} + 1", "1000000000")
        print(f"   ➕ Calculating: {large_num} + 1")
        result = self.calc.add(large_num, 1)
        print(f"   📊 Result: {result}")
        
        # ===== STEP 2: VALIDATE LARGE NUMBER RESULT =====
        self.log_test_step("STEP 2", "Validate large number result", None, "Result should equal 1000000000")
        assert result == 1000000000, f"Expected 1000000000, got {result}"
        print("   ✅ Large numbers test passed")
        
        print("\n🎉 Calculator large numbers test completed successfully!")
    
    @pytest.mark.critical
    def testBasicOperations(self):
        """
        Critical test for basic operations with detailed logging
        """
        print("\n" + "="*80)
        print("🧪 TEST: Calculator Critical Basic Operations")
        print("="*80)
        
        # ===== STEP 1: TEST ADDITION =====
        self.log_test_step("STEP 1", "Test critical addition", "1 + 1", "2")
        print("   ➕ Critical addition: 1 + 1")
        add_result = self.calc.add(1, 1)
        print(f"   📊 Addition result: {add_result}")
        assert add_result == 2, f"Expected 2, got {add_result}"
        print("   ✅ Critical addition passed")
        
        # ===== STEP 2: TEST SUBTRACTION =====
        self.log_test_step("STEP 2", "Test critical subtraction", "3 - 1", "2")
        print("   ➖ Critical subtraction: 3 - 1")
        sub_result = self.calc.subtract(3, 1)
        print(f"   📊 Subtraction result: {sub_result}")
        assert sub_result == 2, f"Expected 2, got {sub_result}"
        print("   ✅ Critical subtraction passed")
        
        # ===== STEP 3: TEST MULTIPLICATION =====
        self.log_test_step("STEP 3", "Test critical multiplication", "2 * 2", "4")
        print("   ✖️ Critical multiplication: 2 * 2")
        mul_result = self.calc.multiply(2, 2)
        print(f"   📊 Multiplication result: {mul_result}")
        assert mul_result == 4, f"Expected 4, got {mul_result}"
        print("   ✅ Critical multiplication passed")
        
        # ===== STEP 4: TEST DIVISION =====
        self.log_test_step("STEP 4", "Test critical division", "4 / 2", "2")
        print("   ➗ Critical division: 4 / 2")
        div_result = self.calc.divide(4, 2)
        print(f"   📊 Division result: {div_result}")
        assert div_result == 2, f"Expected 2, got {div_result}"
        print("   ✅ Critical division passed")
        
        print("\n🎉 Calculator critical basic operations test completed successfully!") 