def reversed_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

input_str = input("Enter a string: ")
output_str = reversed_string(input_str)

print("Reversed String:", output_str)