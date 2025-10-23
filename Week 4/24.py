def rev_each_word(text):
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

input_string = input("Enters: ")
result = rev_each_word(input_string)

print("Original Sentence: ", input_string)
print("Reversed Words: ", result)