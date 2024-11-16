# Create a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# Access a value by key
print(thisdict["model"])

# Add a new item
thisdict["color"] = "red"
print(thisdict)

# Update an item
thisdict["year"] = 2018
print(thisdict)

# Remove an item
thisdict.pop("model")
print(thisdict)

# Get all keys
print(thisdict.keys())

# Get all values
print(thisdict.values())

# Clear the dictionary
thisdict.clear()
print(thisdict)
