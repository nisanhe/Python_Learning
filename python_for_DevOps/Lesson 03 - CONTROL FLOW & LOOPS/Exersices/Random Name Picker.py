import random

names = [input("Enter name: ") for _ in range(4)]
print(f"Random name: {random.choice(names)}")
print(f"All names: {names}")
