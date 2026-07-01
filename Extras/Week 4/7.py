import string

def is_pangram(sentence):
    sentence_letters = set(sentence.lower())
    alphabet = set(string.ascii_lowercase)

    return alphabet.issubset(sentence_letters)


input_sentence = input("Enter a sentence: ")
if is_pangram(input_sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is NOT a pangram.")