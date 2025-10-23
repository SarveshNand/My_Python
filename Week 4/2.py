def remove_duplicates(s):
    result = []
    seen = set()
    for char in s:
        if char not in seen:
            seen.add(seen)
            result.append(char)
    return ''.join(result)

input_str = input("Enter a string: ")
output_str = remove_duplicates(input_str)

print("String after removing duplicates: ", output_str)