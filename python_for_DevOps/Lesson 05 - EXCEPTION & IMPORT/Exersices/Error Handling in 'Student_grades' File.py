def process_grades(filename):
    """Processes grades from a file, handling potential errors."""
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Process each line, handling potential errors within the line
                try:
                    grade = float(line.strip())
                    # Do something with the grade (e.g., calculate average)
                except ValueError:
                    print(f"Invalid grade: {line.strip()}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Example usage:
process_grades("Student_grades.txt")