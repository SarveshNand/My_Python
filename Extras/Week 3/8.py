def count_lines_and_words(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)

            print(f"Total Lines: {line_count}")
            print(f"Total Words: {word_count}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")

filename = input("Enter the filename: ")
count_lines_and_words(filename)