# Create a new file, throws an error if the file already exists
f = open("myfile.txt", "x")

# Create a file if it doesn't exist, or open it for appending
f = open("myfile.txt", "a")

# Create a file if it doesn't exist, or overwrite its content
f = open("myfile.txt", "w")
