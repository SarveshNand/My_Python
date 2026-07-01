import re

def longest_sentence(paragraph):
    # Split paragraph into sentences using punctuation marks (., !, ?)
    sentences = re.split(r'(?<=[.!?])\s+', paragraph.strip())
    
    # Find the sentence with the maximum number of words
    longest = max(sentences, key=lambda s: len(s.split()))
    return longest

paragraph = "Hello! This is a test paragraph. It contains multiple sentences, some short, some much longer than others. Which one is the longest?"

longest_sent = longest_sentence(paragraph)
print("Longest sentence:")
print(longest_sent)