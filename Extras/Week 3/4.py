def handling_filenotfounderror(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("Error: The file has not been found.")

filename = 'sling.txt'
print(handling_filenotfounderror(filename))