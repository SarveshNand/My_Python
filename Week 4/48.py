def display_lines_with_keyword(filename, keyword):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                if keyword.lower() in line.lower():
                    print(f"Line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

filename = 'sample.txt'
keyword = 'python'

display_lines_with_keyword(filename, keyword)