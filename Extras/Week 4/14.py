def to_title_case(text):
    words = text.split()
    title_cased_words = []
    
    for word in words:
        if len(word) > 0:
            # Capitalize the first letter, make the rest lowercase
            title_cased_word = word[0].upper() + word[1:].lower()
            title_cased_words.append(title_cased_word)
        else:
            title_cased_words.append(word)

    # Join the words back into a single string
    return ' '.join(title_cased_words)

input_string = "hELLo woRLd! thiS is a TeSt."
result = to_title_case(input_string)

print("Original:", input_string)
print("Title Case:", result)