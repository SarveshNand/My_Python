# Reverse a String.
# a:str = "hello"
# print(a[::-1])


# Check if a String is a Palindrome.
# a:str = input("")
# if a == a[::-1]:
#     print(True)
# else:
#     print(False)


# Count Vowel in a String.
# a:str = input("Enter a string: ")
# vowels:str = "aeiou"
# count:int = 0
# for char in a:
#     if char in vowels:
#         count += 1
# print("Number of Vowels: " , count)


# Remove all punctuation from a string.
# import string
# a = input("Enter a String: ")
# cleaned = ''.join(char for char in a if char not in string.punctuation)
# print("Without Punctuation: ", cleaned)


# Convert string to title case.
# a = input("Enter a String: ")
# a = a.title()
# print(a)


# Replace all spaces with hyphens.
# a = input("Enter a String: ")
# a = a.replace(" ", "-")
# print(a)


# Count occurrences of each character
# a = input("Enter a String: ")
# char_count = {}
# for char in a:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
# print("Character counts: ", char_count)


# Check if two strings are anagrams.
# a = input("Enter First String: ").replace(" ", "").lower()
# b = input("Enter Second String: ").replace(" ", "").lower()
# if sorted(a) == sorted(b):
#     print(True)
# else:
#     print(False)


# Find the first non-repeating character in a given string.
# from collections import Counter
# a = input("Enter a string: ")
# count = Counter(a)
# for char in a:
#     if count[char] == 1:
#         print("First non-repeating character:", char)
#         break
# else:
#     print("No non-repeating characters found.")


# Check if a string contains only digits.
# a = input("Enter a String: ")
# if a.isdigit():
#     print(True)
# else:
#     print(False)


# Extract all numbers (digits) from a given string.
# import re
# a = input("Enter a string: ")
# numbers = re.findall(r'\d+', a)
# print("Extracted numbers:", numbers)


# Remove duplicate characters from a string.
# a = input("Enter a string: ")
# result = ""
# seen = set()
# for char in a:
#     if char not in seen:
#         seen.add(char)
#         result += char
# print("Without duplicates:", result)


# Check if a string is a valid email address.
# import re
# email = input("Enter an email address: ")
# pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
# if re.match(pattern, email):
#     print("Valid email address.")
# else:
#     print("Invalid email address.")


# Convert camelCase to snake_case.
# import re
# def camel_to_snake(s):
#     snake = re.sub(r'(?<!^)([A-Z])', r'_\1', s).lower()
#     return snake
# a = input("Enter a camelCase string: ")
# print("snake_case:", camel_to_snake(a))


# Capitalize the first letter of each sentence in a paragraph.
# import re
# def capitalize_sentences(text):
#     sentences = re.split('([.!?])', text)
#     result = ""
#     for i in range(0, len(sentences) - 1, 2):
#         sentence = sentences[i].strip().capitalize()
#         punctuation = sentences[i + 1]
#         result += sentence + punctuation + " "
#     if len(sentences) % 2 != 0:
#         result += sentences[-1].strip().capitalize()
#     return result.strip()
# a = input("Enter a paragraph: ")
# print("Formatted paragraph:")
# print(capitalize_sentences(a))