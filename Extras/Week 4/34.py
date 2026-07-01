def check_word_in_file(filename, word):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                # Check if the word is present in the line (case-insensitive)
                if word.lower() in line.lower().split():
                    return True
        return False
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return False

filename = "sample.txt"
word_to_find = "python"

if check_word_in_file(filename, word_to_find):
    print(f"The word '{word_to_find}' was found in the file.")
else:
    print(f"The word '{word_to_find}' was NOT found in the file.")