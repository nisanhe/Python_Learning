import os

# Execute a system command
os.system("ls -la")

# Open a pipe to a process
process = os.popen("ls -la")
output = process.read()
print(output)