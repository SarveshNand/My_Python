import string

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

input_text = "Hello, world! This is Python... #awesome :)"
clean_text = remove_punctuation(input_text)

print("Original:", input_text)
print("Cleaned :", clean_text)