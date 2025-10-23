def has_all_unique_characters(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

input_str = input("Enter a string: ")

if has_all_unique_characters(input_str):
    print("All characters are unique")
else:
    print("The string has duplicate characters")