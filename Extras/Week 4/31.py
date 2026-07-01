def first_non_repeating_char(text):
    char_count = {}

    # Count the frequency of each character
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first character with count 1
    for char in text:
        if char_count[char] == 1:
            return char

    return None  # If all characters repeat

input_string = "swiss"
result = first_non_repeating_char(input_string)

if result:
    print(f"The first non-repeating character is: '{result}'")
else:
    print("There is no non-repeating character.")