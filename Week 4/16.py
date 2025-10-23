def remove_non_alphabets(text):
    filtered_text = ''.join(char for char in text if char.isalpha())
    return filtered_text

input_string = input("Enter: ")
result = remove_non_alphabets(input_string)

print("Original String: ", input_string)
print("Alphabetic Only: ", result)