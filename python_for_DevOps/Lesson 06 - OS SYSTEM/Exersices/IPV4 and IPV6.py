import os
import subprocess

def execute_ipconfig(output_file):
    """
    Executes the ipconfig command and saves the output to a file.

    Args:
        output_file (str): The name of the output file.
    """
    try:
        with open(output_file, 'w') as f:
            subprocess.run(["ipconfig"], stdout=f)
        print(f"ipconfig output saved to '{output_file}'.")
    except Exception as e:
        print(f"Error executing ipconfig command: {e}")

def parse_ipconfig_output(output_file):
    """
    Parses the ipconfig output file and prints IPv4 and IPv6 addresses.

    Args:
        output_file (str): The name of the output file.
    """
    try:
        with open(output_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if "IPv4 Address" in line:
                    ipv4_address = line.split(":")[1].strip()
                    print(f"IPv4 Address: {ipv4_address}")
                elif "IPv6 Address" in line:
                    ipv6_address = line.split(":")[1].strip()
                    print(f"IPv6 Address: {ipv6_address}")
    except FileNotFoundError:
        print(f"File '{output_file}' not found.")

def main():
    """
    Main function to execute the steps.
    """
    output_file = "ipconfig_output.txt"

    execute_ipconfig(output_file)
    parse_ipconfig_output(output_file)
    os.remove(output_file)  # Delete the output file

if __name__ == "__main__":
    main()