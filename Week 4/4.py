def count_case(sentence):
    upper_count = 0
    lower_count = 0

    for char in sentence:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

input_sentence = input("Enter a sentence: ")
upper, lower = count_case(input_sentence)

print("Number of uppercase letters: ", upper)
print("Number of lowercase letters: ", lower)