import os
import subprocess

def create_folder(folder_name):
    """
    Creates a new folder in the current directory.

    Args:
        folder_name (str): The name of the folder to create.
    """
    try:
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")

def navigate_to_folder(folder_name):
    """
    Changes the working directory to the specified folder.

    Args:
        folder_name (str): The name of the folder to navigate to.
    """
    try:
        os.chdir(folder_name)
        print(f"Navigated to '{folder_name}' folder.")
    except FileNotFoundError:
        print(f"Folder '{folder_name}' not found.")

def execute_ping_command(target_website, output_file):
    """
    Executes the ping command and saves the output to a file.

    Args:
        target_website (str): The website to ping.
        output_file (str): The name of the output file.
    """
    try:
        with open(output_file, 'w') as f:
            subprocess.run(["ping", target_website], stdout=f)
        print(f"Ping command output saved to '{output_file}'.")
    except Exception as e:
        print(f"Error executing ping command: {e}")

def analyze_results(output_file):
    """
    Analyzes the ping command output and prints a message.

    Args:
        output_file (str): The name of the output file.
    """
    try:
        with open(output_file, 'r') as f:
            lines = f.readlines()
            if "Reply from" in lines[-1]:
                print("Connection successful!")
            else:
                print("Connection failed.")
    except FileNotFoundError:
        print(f"File '{output_file}' not found.")

def main():
    """
    Main function to execute the steps.
    """
    folder_name = "ping_results"
    target_website = "www.google.com"
    output_file = "ping_output.txt"

    create_folder(folder_name)
    navigate_to_folder(folder_name)
    execute_ping_command(target_website, output_file)
    analyze_results(output_file)

if __name__ == "__main__":
    main()