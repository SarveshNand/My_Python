def count_vowels(paragraph):
    vowels = 'aeiou'
    counts = {vowel: 0 for vowel in vowels}

    for char in paragraph.lower():
        if char in counts:
            counts[char] += 1

    return counts

paragraph = """This is a sample paragraph to demonstrate how many vowels are present in this text."""

vowel_counts = count_vowels(paragraph)
print("Vowel counts:")
for vowel, count in vowel_counts.items():
    print(f"{vowel}: {count}")