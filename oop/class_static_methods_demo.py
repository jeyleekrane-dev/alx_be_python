"""
class_static_methods_demo.py

This script defines a Calculator class with a static method and a class method
to demonstrate their distinct use cases.
"""


class Calculator:
    """
    A class to perform simple arithmetic operations using static and class methods.
    """
    # A class attribute that can be accessed by class methods
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method that takes two numbers and returns their sum.
        It does not have access to the class or instance state.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method that takes the class itself (cls) as its first argument.
        It can access and modify class attributes. Here, it prints a class attribute
        before performing multiplication.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
