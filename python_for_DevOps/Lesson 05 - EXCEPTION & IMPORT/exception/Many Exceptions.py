# Example : Print one message if the try block raises a NameError and another for other errors:
try: print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")