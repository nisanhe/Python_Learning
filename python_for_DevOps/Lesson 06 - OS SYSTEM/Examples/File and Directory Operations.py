import os

# Get current working directory
current_dir = os.getcwd()
print(current_dir)

# Change directory
os.chdir("/path/to/new/directory")

# List files and directories
files_and_dirs = os.listdir(".")
print(files_and_dirs)

# Create a directory
os.mkdir("new_directory")

# Remove a file
os.remove("file_to_remove.txt")

# Check if a file exists
if os.path.isfile("file.txt"):
    print("File exists")