# Integer, float, and complex types
num1 = 5
print(num1, "is of type", type(num1))

num2 = 2.0
print(num2, "is of type", type(num2))

num3 = 1 + 2j
print(num3, "is of type", type(num3))

# Output:
# 5 is of type <class 'int'>
# 2.0 is of type <class 'float'>
# (1+2j) is of type <class 'complex'>

# Type casting examples
x = int('100')
f = float('5.5')
s = str('1')

print(x)  # Output: 100
print(f)  # Output: 5.5
print(s)  # Output: "1"

# Concatenating strings
s = '1' + '5'
print(s)  # Output: "15"
