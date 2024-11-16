# Create a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Access tuple items
print(thistuple[1])  # Second item

# Length of a tuple
print(len(thistuple))

# Tuple with one item
one_item_tuple = ("apple",)
print(type(one_item_tuple))  # <class 'tuple'>

# Combine two tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Unpack a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
