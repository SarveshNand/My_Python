def average_word_length(sentence):
    words = sentence.split()
    if not words:
        return 0
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

input_sentence = "Calculate the average length of each word"
avg_length = average_word_length(input_sentence)
print(f"Average word length: {avg_length}")