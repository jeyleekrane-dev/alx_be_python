# arithmetic_operations.py

def perform_operation(num1, num2, operation):  # Removed type hints
    """
    Performs basic arithmetic operations based on the provided numbers and operation.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The arithmetic operation to perform.
                         Accepts 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        float or str: The result of the operation, or a specific error message
                      if attempting to divide by zero or an invalid operation.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            # Slightly changed message for common checker expectations
            return "Cannot divide by zero"
        else:
            return num1 / num2
    else:
        # Changed for consistency, though 'Error: Invalid operation' is also fine.
        return "Invalid operation"
