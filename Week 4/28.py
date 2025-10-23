def count_word_frequencies(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()

        # Normalize text: lower case and remove punctuation
        import string
        text = text.lower()
        for punct in string.punctuation:
            text = text.replace(punct, '')

        words = text.split()

        # Count word frequencies using a dictionary
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        return word_freq

    except FileNotFoundError:
        return f"File '{filename}' not found."

filename = "sample.txt"  # Make sure this file exists in the same directory
frequencies = count_word_frequencies(filename)

# Display result
if isinstance(frequencies, dict):
    for word, count in sorted(frequencies.items()):
        print(f"{word}: {count}")
else:
    print(frequencies)