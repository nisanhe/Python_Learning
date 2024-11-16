# Example : Try to open and write to a file that is not writable:
try:
    f = open("demofile.txt")
try:
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()
except:
    print("Something went wrong when opening the file")


    # try:
    #     # code that might raise an exception
    #     x = 5 / 0
    # except ZeroDivisionError:
    #     # handle the exception
    #     print("Error: Division by zero is not allowed")
    # else:
    #     # code that will run if no exception is raised
    #     print("No exception was raised")
    # finally:
    #     # code that will run regardless of whether an exception was raised or not
    #     print("This code will run regardless of whether an exception was raised or not")
    