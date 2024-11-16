import os

# Get an environment variable
user_name = os.getenv("USER")
print(user_name)

# Set an environment variable (temporary)
os.environ["MY_VARIABLE"] = "Hello, world!"
print(os.environ["MY_VARIABLE"])