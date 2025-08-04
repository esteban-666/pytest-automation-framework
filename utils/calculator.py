"""
Calculator utility class for mathematical operations.
"""
import math
from typing import List


class Calculator:
    """Simple calculator class for mathematical operations."""
    
    def __init__(self):
        """Initialize calculator with empty history."""
        self.history: List[str] = []
    
    def add(self, a: float, b: float) -> float:
        """
        Add two numbers.
        
        Args:
            a: First number
            b: Second number
        
        Returns:
            Sum of the two numbers
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """
        Subtract second number from first number.
        
        Args:
            a: First number
            b: Second number
        
        Returns:
            Difference of the two numbers
        """
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """
        Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
        
        Returns:
            Product of the two numbers
        """
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """
        Divide first number by second number.
        
        Args:
            a: First number (dividend)
            b: Second number (divisor)
        
        Returns:
            Quotient of the division
        
        Raises:
            ValueError: If divisor is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, base: float, exponent: float) -> float:
        """
        Raise base to the power of exponent.
        
        Args:
            base: Base number
            exponent: Exponent
        
        Returns:
            Base raised to the power of exponent
        """
        result = math.pow(base, exponent)
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result
    
    def sqrt(self, number: float) -> float:
        """
        Calculate square root of a number.
        
        Args:
            number: Number to find square root of
        
        Returns:
            Square root of the number
        
        Raises:
            ValueError: If number is negative
        """
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        
        result = math.sqrt(number)
        self.history.append(f"√{number} = {result}")
        return result
    
    def get_history(self) -> List[str]:
        """
        Get calculation history.
        
        Returns:
            List of calculation history entries
        """
        return self.history.copy()
    
    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()
    
    def get_last_result(self) -> float:
        """
        Get the result of the last calculation.
        
        Returns:
            Last calculation result
        
        Raises:
            ValueError: If no calculations have been performed
        """
        if not self.history:
            raise ValueError("No calculations performed yet")
        
        # Extract the result from the last history entry
        last_entry = self.history[-1]
        result_str = last_entry.split(" = ")[-1]
        return float(result_str) 