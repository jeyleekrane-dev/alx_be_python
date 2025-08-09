"""
library_system.py

This module defines a Book base class, EBook and PrintBook derived classes
to demonstrate inheritance, and a Library class to demonstrate composition.
"""


class Book:
    """
    Base class for all books.
    """

    def __init__(self, title, author):
        """
        Initializes a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a user-friendly string representation for the Book class.
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Derived class representing an e-book.
    Inherits from the Book class.
    """

    def __init__(self, title, author, file_size):
        """
        Initializes an EBook instance, calling the base class constructor
        and adding a file_size attribute.

        Args:
            title (str): The title of the e-book.
            author (str): The author of the e-book.
            file_size (int): The size of the e-book file in KB.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Returns a user-friendly string representation for the EBook class.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Derived class representing a physical print book.
    Inherits from the Book class.
    """

    def __init__(self, title, author, page_count):
        """
        Initializes a PrintBook instance, calling the base class constructor
        and adding a page_count attribute.

        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The number of pages in the book.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Returns a user-friendly string representation for the PrintBook class.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Class demonstrating composition. It contains a collection of Book objects.
    """

    def __init__(self):
        """
        Initializes a Library with an empty list to store books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a Book, EBook, or PrintBook instance to the library's collection.

        Args:
            book (Book): An instance of a book to add.
        """
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def list_books(self):
        """
        Prints the details of each book in the library by relying on
        the __str__ method of each book object.
        """
        print("\n--- Listing all books in the library ---")
        for book in self.books:
            print(book)
        print("--- End of list ---")
