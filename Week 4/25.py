def every_third_char(text):
    return text[2::3]  # Start from index 2 and take every 3rd character

input_string = input("Enter: ")
result = every_third_char(input_string)

print("Original String: ", input_string)
print("Every 3rd Char: ", result)