def count_frequency(n):
    frequency = {}
    for char in n:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

input_str = input("Enter a string: ")
output_str = count_frequency(input_str)

print("Character frequencies: ")
for char, freq in output_str.items():
    print(f"{char} : {freq}")