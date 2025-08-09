"""
polymorphism_demo.py

This script defines a base class Shape and two derived classes, Rectangle and Circle,
to demonstrate polymorphism through method overriding.
"""
import math


class Shape:
    """
    A base class for different geometric shapes.
    It defines a common interface with the area() method.
    """

    def area(self):
        """
        Calculates the area of the shape. This method should be
        overridden by any derived classes.
        """
        raise NotImplementedError("Subclass must implement abstract method")


class Rectangle(Shape):
    """
    A derived class representing a rectangle.
    It overrides the area() method to calculate a rectangle's area.
    """

    def __init__(self, length, width):
        """
        Initializes a Rectangle instance.

        Args:
            length (int or float): The length of the rectangle.
            width (int or float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.length * self.width


class Circle(Shape):
    """
    A derived class representing a circle.
    It overrides the area() method to calculate a circle's area.
    """

    def __init__(self, radius):
        """
        Initializes a Circle instance.

        Args:
            radius (int or float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.
        """
        return math.pi * self.radius ** 2
