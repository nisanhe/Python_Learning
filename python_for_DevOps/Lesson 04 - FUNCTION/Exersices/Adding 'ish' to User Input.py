def add_ish(word):
    """Adds 'ish' to the end of a given word."""
    return word + "ish"

while True:
    user_input = input("Enter a word (or 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    else:
        result = add_ish(user_input)
        print(result)