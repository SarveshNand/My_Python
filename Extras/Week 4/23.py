# Common stop words list (can be extended)
stop_words = {
    "a", "an", "the", "and", "or", "but", "if", "while", "with", "to",
    "of", "in", "on", "for", "at", "by", "from", "up", "about", "as",
    "into", "like", "through", "after", "over", "between", "out", "against",
    "during", "without", "before", "under", "around", "among"
}

def remove_stop_words(sentence):
    words = sentence.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

input_sentence = "This is a simple example of a sentence with some stop words."
result = remove_stop_words(input_sentence)

print("Original Sentence:", input_sentence)
print("After Removing Stop Words:", result)