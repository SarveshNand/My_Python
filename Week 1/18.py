char = input("Enter a character: ")
char = char.lower()
if char in 'aeiou':
    print(f"{char} is a vowel")
elif char.isalpha():
    print(f"{char} is a consonant")
else:
    print(f"{char} is an invalid character")