def clean_text_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        cleaned_lines = []
        for line in lines:
            # Strip leading/trailing spaces and replace multiple spaces with a single space
            stripped_line = ' '.join(line.strip().split())
            if stripped_line:  # Ignore blank lines
                cleaned_lines.append(stripped_line)

        # Write cleaned lines back to the file
        with open(filename, 'w', encoding='utf-8') as file:
            for line in cleaned_lines:
                file.write(line + '\n')

        print(f"File '{filename}' cleaned successfully.")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

filename = 'sample.txt'
clean_text_file(filename)