# Example : Raise an error and stop the program if x is lower than 0:
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")


    # Example : Raise a TypeError if x is not an integer:
w = "hello"
if not type(w) is int:
    raise TypeError("Only integers are allowed")