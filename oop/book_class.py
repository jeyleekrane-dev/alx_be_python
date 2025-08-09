"""
book_class.py

This script defines the Book class with a constructor, a destructor,
and magic methods for string representation.
"""


class Book:
    """
    A class to represent a book with its title, author, and publication year.
    """

    def __init__(self, title, author, year):
        """
        Constructor to initialize a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.")

    def __del__(self):
        """
        Destructor that is called when the Book object is about to be destroyed.
        It prints a message indicating which book is being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns a user-friendly string representation of the Book instance.
        This is what is displayed when you use `print(book_instance)`.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an official string representation that can be used to
        recreate the object. This is typically used by developers for debugging.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Note: The main.py script provided in the prompt will be used to test this class.
# This file does not need to be run directly.
