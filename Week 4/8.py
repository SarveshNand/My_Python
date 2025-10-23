def sort_words_in_sentence(sentence):
    words = sentence.split()
    
    # Sort the words alphabetically
    sorted_words = sorted(words, key=lambda word: word.lower())  # Case-insensitive sort
    
    # Join the sorted words back into a sentence
    sorted_sentence = ' '.join(sorted_words)
    
    return sorted_sentence

sentence = "The quick brown fox jumps over the lazy dog"
sorted_sentence = sort_words_in_sentence(sentence)
print("Original Sentence:", sentence)
print("Sorted Sentence:", sorted_sentence)