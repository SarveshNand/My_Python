def pig_latin(word):
    vowels = "aeiou"
    word = word.lower()
    if word[0] in vowels:
        return word + "way"
    else:
        # Find the position of the first vowel
        for i, char in enumerate(word):
            if char in vowels:
                return word[i:] + word[:i] + "ay"
        # No vowels found (rare case)
        return word + "ay"

def sentence_to_pig_latin(sentence):
    words = sentence.split()
    pig_latin_words = [pig_latin(word) for word in words]
    return ' '.join(pig_latin_words)

input_sentence = "Hello world this is VSCode"
output_sentence = sentence_to_pig_latin(input_sentence)
print(output_sentence)