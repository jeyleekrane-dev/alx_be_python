"""
This script defines and runs unit tests for the SimpleCalculator class
found in simple_calculator.py.
"""
import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """
    Test cases for the SimpleCalculator class.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test method runs.
        This ensures each test starts with a fresh instance.
        """
        self.calc = SimpleCalculator()

    def test_add(self):
        """
        Test the add method with various inputs, including positive,
        negative, and zero numbers.
        """
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(10.5, 2.5), 13.0)

    def test_subtract(self):
        """
        Test the subtract method with various inputs.
        """
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(0, 7), -7)
        self.assertEqual(self.calc.subtract(10.5, 5.25), 5.25)

    def test_multiply(self):
        """
        Test the multiply method with various inputs, including multiplication
        by zero and negative numbers.
        """
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(-4, -4), 16)
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

    def test_divide(self):
        """
        Test the divide method, including normal division and the critical
        edge case of division by zero.
        """
        # Test normal division
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(10, 4), 2.5)
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(12.5, 2.5), 5.0)

        # Test division by zero, which should return None as per the class's docstring
        self.assertIsNone(self.calc.divide(10, 0))


if __name__ == '__main__':
    unittest.main()
