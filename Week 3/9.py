import csv

def read_csv_file(filename):
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            print("CSV File Contents:\n")
            for row in reader:
                print(', '.join(row))  # Print each row as comma-separated values
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")

# Example usage
filename = input("Enter the CSV filename: ")
read_csv_file(filename)