def find_and_replace(filename, old_text, new_text):
    try:
        # Read the file content
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        # Replace old_text with new_text
        updated_content = content.replace(old_text, new_text)

        # Write the updated content back to the file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        print(f"Replaced all occurrences of '{old_text}' with '{new_text}' in {filename}.")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

filename = "sample.txt"
old_text = "hello"
new_text = "hi"

find_and_replace(filename, old_text, new_text)