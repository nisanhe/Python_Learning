def multiply_by_two(number):
    """Multiplies a number by 2."""
    return number * 2

def add_numbers(num1, num2):
    """Adds two numbers."""
    return num1 + num2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result1 = multiply_by_two(num1)
result2 = multiply_by_two(num2)
final_result = add_numbers(result1, result2)

print("The final result is:", final_result)