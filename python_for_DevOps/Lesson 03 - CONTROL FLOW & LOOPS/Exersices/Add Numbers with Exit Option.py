while True:
    user_input = input("Enter two numbers separated by space (or type 'EXIT' to quit): ")
    if user_input.upper() == "EXIT":
        print("Thanks, have a good day.")
        break
    try:
        a, b = map(int, user_input.split())
        print(f"The sum is: {a + b}")
    except ValueError:
        print("Invalid input, please try again.")
