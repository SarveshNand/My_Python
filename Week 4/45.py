import re
from collections import Counter

def find_duplicate_words(paragraph):
    # Convert paragraph to lowercase and split into words using regex to avoid punctuation
    words = re.findall(r'\b\w+\b', paragraph.lower())
    
    # Count frequency of each word
    word_counts = Counter(words)
    
    # Extract words with count > 1 (duplicates)
    duplicates = [word for word, count in word_counts.items() if count > 1]
    return duplicates

paragraph = "This is a test. This test is simple, but it is a good test."

duplicates = find_duplicate_words(paragraph)
print("Duplicate words:", duplicates)