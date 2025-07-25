# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations based on the provided numbers and operation.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The arithmetic operation to perform.
                         Accepts 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        float or str: The result of the operation, or "Error: Division by zero"
                      if attempting to divide by zero.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"
