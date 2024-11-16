# Create a set
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Add an item
thisset.add("orange")
print(thisset)

# Add items from another collection
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# Remove an item
thisset.discard("banana")  # No error if item not found
print(thisset)

# Clear the set
thisset.clear()
print(thisset)
