def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File Contents:\n")
            print(contents)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")

filename = input("Enter the filename (with path if needed): ")
read_file(filename)