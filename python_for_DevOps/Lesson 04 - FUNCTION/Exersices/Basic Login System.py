users = [
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"}
]

def login(username, password):
    """Checks if the username and password are valid."""
    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
    return False

username = input("Enter your username: ")
password = input("Enter your password: ")

if login(username, password):
    print("Login successful!")
else:
    print("Invalid username or password.")