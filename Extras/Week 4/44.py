import re

def extract_integers(text):
    # Find all sequences of digits (including negative numbers if needed)
    integers = re.findall(r'-?\d+', text)
    # Convert them to int type
    return [int(num) for num in integers]

sample_text = "There are 12 apples, -5 oranges, and 30 bananas in the basket."

numbers = extract_integers(sample_text)
print("Extracted integers:", numbers)