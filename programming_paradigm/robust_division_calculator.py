"""
This module provides a safe division function that handles
common errors like division by zero and non-numeric input.
"""


def safe_divide(numerator, denominator):
    """
    Divides a numerator by a denominator, handling various errors.

    Args:
        numerator (str): The string representation of the numerator.
        denominator (str): The string representation of the denominator.

    Returns:
        str: A message indicating the result of the division or the error encountered.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Perform the division
        result = num / den

        return f"The result of the division is {result}"

    except ValueError:
        # Catch errors where the input cannot be converted to a number
        return "Error: Invalid input. Both numerator and denominator must be numeric."
    except ZeroDivisionError:
        # Catch the specific case of division by zero
        return "Error: Cannot divide by zero."
    except Exception as e:
        # Catch any other unexpected errors
        return f"An unexpected error occurred: {e}"
