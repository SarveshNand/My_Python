def find_longest_word(sentence):
    words = sentence.split()
    if not words:
        return None
    
    longest = max(words, key=len)
    return longest

input_sentence = input("Enter a sentence: ")
longest_word = find_longest_word(input_sentence)

if longest_word:
    print("The longest word is:", longest_word)
    print("Length:", len(longest_word))
else:
    print("No words found in the input.")