def factorial(n):
    """Calculates the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
try:
    result = factorial(-5)
    print("Factorial:", result)
except ValueError as e:
    print(e)