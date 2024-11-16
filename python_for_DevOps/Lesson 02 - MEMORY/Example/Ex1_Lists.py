# Create a list
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Access the second item
print(thislist[1])

# Access the last item
print(thislist[-1])

# Access a range of items
print(thislist[0:2])  # Includes index 0 and 1, but not 2

# Change an item
thislist[1] = "blackcurrant"
print(thislist)

# Add an item
thislist.append("orange")
print(thislist)

# Insert an item at a specific index
thislist.insert(2, "watermelon")
print(thislist)

# Extend the list with another list
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Remove an item
thislist.remove("banana")
print(thislist)

# Remove an item by index
thislist.pop(1)
print(thislist)

# Clear the list
thislist.clear()
print(thislist)
