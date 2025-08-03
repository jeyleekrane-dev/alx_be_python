"""
This module implements a simple library management system using Python classes.
It defines a Book class and a Library class to manage a collection of books.
"""


class Book:
    """
    A class to represent a book with a title, author, and availability status.
    """

    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        # Private attribute to track the book's availability.
        self._is_checked_out = False

    def check_out(self):
        """
        Checks out the book, marking it as unavailable.
        """
        self._is_checked_out = True

    def return_book(self):
        """
        Returns the book, marking it as available again.
        """
        self._is_checked_out = False

    def is_available(self):
        """
        Checks if the book is currently available.

        Returns:
            bool: True if the book is available, False otherwise.
        """
        return not self._is_checked_out


class Library:
    """
    A class to manage a collection of Book objects.
    """

    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self._books = []

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): The Book object to add.
        """
        self._books.append(book)
        print(f"Added '{book.title}' to the library.")

    def check_out_book(self, title):
        """
        Checks out a book from the library by its title.

        Args:
            title (str): The title of the book to check out.
        """
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f"Checked out '{title}'.")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"Sorry, '{title}' was not found in the library.")

    def return_book(self, title):
        """
        Returns a book to the library by its title.

        Args:
            title (str): The title of the book to return.
        """
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    print(f"Returned '{title}'.")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"Sorry, '{title}' was not found in the library.")

    def list_available_books(self):
        """
        Prints a list of all available books in the library.
        """
        found_available_books = False
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
                found_available_books = True

        if not found_available_books:
            print("No books are currently available.")
