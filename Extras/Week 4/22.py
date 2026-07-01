def count_words_starting_with_vowel(text):
    vowels = 'aeiouAEIOU'
    words = text.split()
    count = 0
    
    for word in words:
        if len(word) > 0 and word[0] in vowels:
            count += 1
    
    return count

input_string = "An example of a simple string with some words starting with vowels."
result = count_words_starting_with_vowel(input_string)

print(f"Number of words starting with a vowel: {result}")