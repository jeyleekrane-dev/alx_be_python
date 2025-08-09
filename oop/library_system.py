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
        Prints the details of each book in the library, handling
        the different book types.
        """
        print("\n--- Listing all books in the library ---")
        for book in self.books:
            if isinstance(book, EBook):
                print(
                    f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(
                    f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            elif isinstance(book, Book):
                print(f"Book: {book.title} by {book.author}")
        print("--- End of list ---")
