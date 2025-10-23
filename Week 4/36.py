def all_digits(text):
    return text.isdigit()

input_str = input("Enter a string: ")
if all_digits(input_str):
    print("All characters are digits.")
else:
    print("Not all characters are digits.")