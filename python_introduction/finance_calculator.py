# Create a file named finance_calculator.py

# --- User Input for Financial Details ---
# Prompt the user for their monthly income.
# Convert the input string to a float to handle potential decimal values.
monthly_income_str = (input("Enter your monthly income: "))
monthly_income = float(monthly_income_str)

# Ask for their total monthly expenses.
# Convert the input string to a float.
monthly_expenses_str = (input("Enter your total monthly expenses: "))
monthly_expenses = float(monthly_expenses_str)

# --- Calculate Monthly Savings ---
# Calculate the monthly savings by subtracting expenses from income.
monthly_savings = monthly_income - monthly_expenses

# --- Project Annual Savings ---
# Assume a simple annual interest rate of 5%.
annual_interest_rate = 0.05

# Calculate the projected savings after one year, incorporating the interest.
# First, calculate savings over 12 months without interest.
savings_without_interest = monthly_savings * 12
# Then, calculate the interest earned on those 12 months of savings.
interest_earned = savings_without_interest * annual_interest_rate
# Finally, add the interest earned to the savings without interest to get projected savings.
projected_savings = savings_without_interest + interest_earned

# --- Output Results ---
# Display the user's monthly savings.
# Use an f-string to format the output with the calculated monthly_savings.
# Using {:.2f} to format the float to two decimal places for currency.
print(f"Your monthly savings are ${monthly_savings:.2f}.")

# Display the projected annual savings after including interest.
# Use an f-string to format the output with the calculated projected_savings.
# Using {:.2f} to format the float to two decimal places for currency.
print(
    f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
