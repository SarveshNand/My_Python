def generate_acronym(sentence):
    words = sentence.split()
    acronym = ''.join(word[0].upper() for word in words if word)
    return acronym

sentence = "greatest of all time"
acronym = generate_acronym(sentence)

print(f"Acronym for {sentence} is: {acronym}")