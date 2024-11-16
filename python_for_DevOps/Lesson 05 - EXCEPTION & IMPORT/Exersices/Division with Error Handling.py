def division(a, b):
    """Divides two numbers and handles potential ZeroDivisionError."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

# Example usage:
num1 = 10
num2 = 0

result = division(num1, num2)
if result is not None:
    print("Result:", result)