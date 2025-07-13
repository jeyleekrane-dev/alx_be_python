# Create a file named future_age_calculator.py

# Prompt the user to input their current age
# The input() function reads a line from input, converts it to a string, and returns it.
# We then convert this string to an integer using int() because we'll perform arithmetic operations.
current_age_str = input("How old are you? ")
current_age = int(current_age_str)

# Calculate how old the user will be in the year 2050.
# Assuming the current year is 2023, the difference to 2050 is 27 years (2050 - 2023 = 27).
age_in_2050 = current_age + 27

# Print the user's age in 2050 in the specified format.
# An f-string is used for easy embedding of the 'age_in_2050' variable's value.
print(f"In 2050, you will be {age_in_2050} years old.")
