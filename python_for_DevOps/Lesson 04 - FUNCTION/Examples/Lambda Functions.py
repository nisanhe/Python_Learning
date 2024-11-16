
# lambda function is a small anonymous function that can take any number of arguments, but can only have
# one expression. It is used to perform a simple operation on a variable or a set of variables
# lambda arguments : expression
add_ten = lambda a: a + 10
# call the function with argument 5
print(add_ten(5))  # Output: 15

# ==================
y = lambda a, b : a * b
print(y(5, 6))
# ==================
z = lambda a, b, c : a + b + c
print(z(5, 6, 2)