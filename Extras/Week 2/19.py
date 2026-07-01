import string

def remove_punctuation(text):
    return ''.join(char for char in text if char not in string.punctuation)

sample_text = input("Enter: ")
clean_text = remove_punctuation(sample_text)
print(clean_text)