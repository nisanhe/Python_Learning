import os
import subprocess

def execute_command(command, file_name):
    """
    Executes a command and saves the output to a file.

    Args:
        command (str): The command to execute.
        file_name (str): The name of the file to save the output to.
    """
    with open(file_name, 'w') as f:
        subprocess.run(command, shell=True, stdout=f)

def print_file_contents(file_name):
    """
    Prints the contents of a file.

    Args:
        file_name (str): The name of the file to print.
    """
    with open(file_name, 'r') as f:
        print(f.read())

def main():
    """
    Main function to execute the commands and print the results.
    """
    target_website = "www.google.com"  # Replace with your desired website

    # Execute ping command
    ping_command = f"ping {target_website}"
    execute_command(ping_command, "ping_output.txt")

    # Execute ipconfig command (Windows)
    ipconfig_command = "ipconfig"
    execute_command(ipconfig_command, "ipconfig_output.txt")

    # Execute tracert command
    tracert_command = f"tracert {target_website}"
    execute_command(tracert_command, "tracert_output.txt")

    # Print the contents of the files
    print("\nPing Output:\n")
    print_file_contents("ping_output.txt")

    print("\nIPConfig Output:\n")
    print_file_contents("ipconfig_output.txt")

    print("\nTracert Output:\n")
    print_file_contents("tracert_output.txt")

if __name__ == "__main__":
    main()