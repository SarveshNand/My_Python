import re

def count_sentences(paragraph):
    # Split paragraph by sentence-ending punctuation followed by space(s)
    sentences = re.split(r'[.!?]+', paragraph.strip())
    # Remove empty strings from list (in case paragraph ends with punctuation)
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)

paragraph = "Hello! How are you doing today? I hope all is well. Have a nice day."

num_sentences = count_sentences(paragraph)
print(f"Number of sentences: {num_sentences}")