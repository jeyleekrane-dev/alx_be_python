# explore_datetime.py

from datetime import datetime, timedelta


def display_current_datetime():
    """
    Obtains the current date and time, and prints it in "YYYY-MM-DD HH:MM:SS" format.
    """
    # Get the current date and time
    current_date = datetime.now()

    # Format the current date and time
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # Print the formatted current date and time
    print(f"Current date and time: {formatted_current_date}")


def calculate_future_date():
    """
    Prompts the user for a number of days, calculates a future date based on
    the current date, and prints it in "YYYY-MM-DD" format.
    """
    while True:
        try:
            # Prompt the user to enter a number of days
            days_to_add_str = input(
                "Enter the number of days to add to the current date: ")
            days_to_add = int(days_to_add_str)
            break  # Exit loop if input is a valid integer
        except ValueError:
            print("Invalid input. Please enter an integer for the number of days.")

    # Get the current date (without time for simpler future date calculation)
    # Or, if we want to add days to the exact current_date from display_current_datetime,
    # we should pass it or re-get it. For this task, re-getting `now()` is fine.
    current_moment = datetime.now()

    # Calculate the future date by adding the specified number of days
    future_date = current_moment + timedelta(days=days_to_add)

    # Format the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    # Print the future date
    print(f"Future date: {formatted_future_date}")


if __name__ == "__main__":
    # Part 1: Display the Current Date and Time
    display_current_datetime()

    # Part 2: Calculate a Future Date
    calculate_future_date()
