def replace_space_to_underscore(text):
    replaced = text.replace(' ', '_')
    return replaced

input_string = input("Enter: ")
print(replace_space_to_underscore(input_string))