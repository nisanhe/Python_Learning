import shutil

# Copy a file
shutil.copy("source_file.txt", "destination_file.txt")

# Move a file
shutil.move("source_file.txt", "destination_dir")

# Copy a directory recursively
shutil.copytree("source_dir", "destination_dir")