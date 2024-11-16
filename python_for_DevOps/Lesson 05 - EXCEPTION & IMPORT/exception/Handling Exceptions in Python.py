try:
    x = 1/0
except ZeroDivisionError:
    print("You can't divide by zero!")

#     Example :
# The try block will generate an exception, because x is not defined:
try:
    print(t)
except:
    print("An exception occurred!")