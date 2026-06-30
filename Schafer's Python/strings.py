# Practice questions based on the Strings topic.

# Beginner

# 1. Greeting
# Store your name in a variable and print:
# Hello, My name is Aryan

# name = "Sarvesh"
# print(name)

# 2. Full Name
# Store your first name and last name separately and combine them into a full name.

# first_name = "Sarvesh"
# last_name = "nand"
# full_name = first_name + " " + last_name
# print(full_name)

# 3. String Length
# Print the length of a string.

# print(len(full_name))

# 4. Character Indexing
# Print:
# - First character
# - Middle character
# - Last character

# print(full_name[0])
# print(full_name[6:7])
# print(full_name[-1])

# 5. Reverse a String
# Reverse a string using slicing.

# print(full_name[::-1])

# 6. Every Second Character
# Print every second character of a string.

# print(full_name[::2])

# 7. Change Case
# Convert a string to:
# - Uppercase
# - Lowercase
# - Title Case

# print(full_name.upper())
# print(full_name.lower())
# print(full_name.title())

# 8. Count Characters
# Count how many times the letter "'a'" appears in a string.

# print(full_name.count('a'))

# 9. Replace Spaces
# Replace every space with "-".

# print(full_name.replace(" ", "-"))

# 10. Remove Extra Spaces
# Remove leading and trailing spaces from:
# "    Hello World    "

# print("    Hello World    ".strip())



# Intermediate

'''
11. Email Parser

Given:

email = "john@gmail.com"

Extract:

- Username
- Domain
'''

# email = "john@gmail.com"
# username = email[:4]
# domain = email[5:]
# print("Username: " + username, "Domain: " + domain)

# 12. Check Prefix
# Check whether a string starts with ""https"".

# print(full_name.startswith("https"))

# 13. Check File Extension
# Check whether a filename ends with "".py"".

# print(full_name.endswith(".py"))

'''
14. Split Sentence

Given:

sentence = "Python is awesome"

Split it into words.
'''

# sentence = "Python is awesome"
# words = sentence.split(" ")
# print(f"Word 1: {words[0]}\nWord 2: {words[1]}\nWord 3: {words[2]}")

'''
15. Join Words

Join this list into a sentence:

["I", "love", "Python"]
'''

# l = ["I", "love", "Python"]
# print(" ".join(l))

# 16. User Introduction
# Ask the user for their name and age, then print:
# Hello Aryan, you are 18 years old.

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hello {name}, you are {age} years old.")

# 17. Price Display
# Use an f-string to display:
# The price of Laptop is ₹55000.

# price = 55000
# print(f"The price of Laptop is ₹{price}")

# 18. Word Counter
# Count the number of words in a sentence.

# sentence = input("Enter: ")
# word_count = len(sentence.split())
# print(word_count)

# 19. Remove Vowels
# Remove all vowels from a string.

# sentence = input("Enter: ")
# vowels = "aeiouAEIOU"
# result = ''.join([c for c in sentence if c not in vowels])
# print(result)

# 20. Case-Insensitive Comparison
# Check if two strings are equal while ignoring case.

# first_string = input("Enter: ").lower()
# second_string = input("Enter: ").lower()
# print(first_string ==  second_string)


# Challenging

'''
21. Palindrome Checker

Examples:

madam -> True
hello -> False
'''

# string = input("Enter: ")
# rev_string = string[::-1]
# print(string == rev_string)

'''
22. Count Vowels and Consonants

Count vowels and consonants separately.
'''

# vowel_counter = 0
# consonant_counter = 0
# sentence = input("Enter: ")
# vowels = "aeiouAEIOU"
# for c in sentence:
#   if c in vowels:
#     vowel_counter += 1
#   else:
#     consonant_counter += 1
# print(f"Vowels Count: {vowel_counter}\nConsonants Count: {consonant_counter}")

'''
23. Longest Word

Find the longest word in a sentence.
'''

# sentence = input("Enter: ")
# longest_word = max(sentence.split(), key=len)
# print(longest_word)

'''
24. Capitalize Without ".title()"

Capitalize the first letter of every word without using ".title()".
'''

# sentence = input("Enter: ")
# result = ' '.join([word.capitalize() for word in sentence.split()])
# print(result)

'''
25. Print Words Line by Line

Ask the user for a sentence and print each word on a new line.
'''

# sentence = input("Enter: ")
# words = sentence.split()
# for word in words:
#   print(f"{word}")

'''
26. Character Index Finder

Find the index of every occurrence of a character.
'''

# sentence = input("Enter a sentence: ")
# char_to_find = input("Enter character to find: ")
# indices = []
# for i in range(len(sentence)):
#   if sentence[i] == char_to_find:
#     indices.append(i)
# print(f"Indices: {indices}")

'''
27. Phone Number Masker

Input:

9876543210

Output:

******3210
'''

# phone = input("Enter phone number: ")
# if len(phone) > 4:
#   masked_part = '*' * (len(phone) - 4)
#   visible_part = phone[-4:]
#   print(masked_part + visible_part)
# else:
#   print('*' * len(phone))

'''
28. Reverse Word Order

Input:

I love Python

Output:

Python love I
'''

# words = input("Enter: ")
# split_words = words.split()
# rev_word = ' '.join(split_words[::-1])
# print(rev_word)

'''
29. Remove Duplicate Characters

Input:

programming

Output:

progamin
'''

# sentence = input("Enter: ")
# unique_word = []
# for i in sentence:
#   if i not in unique_word:
#     unique_word.append(i)
# unique_word_in_sentence = ''.join(unique_word)
# print(unique_word_in_sentence)

'''
30. Character Frequency Counter

Input:

banana

Output:

b : 1
a : 3
n : 2
'''

# text = input("Enter: ")
# counts = {}
# for char in text:
#   counts[char] = counts.get(char, 0) + 1
# for char, count in counts.items():
#   print(f"{char} : {count}")



# Mini Projects

'''
1. Username Generator

Ask the user for:

- First Name
- Last Name
- Birth Year

Generate usernames like:

aryan2007
a_sharma07
aryan.sharma
'''

# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")
# birth_year = input("Enter birth year: ")
# print(first_name+birth_year)
# print(first_name[0]+"_"+last_name+birth_year)
# print(first_name+"."+last_name)

'''
2. Email Parser

Input:

someone123@gmail.com

Output:

Username: someone123
Domain: gmail.com
'''

# email = input("Email: ")
# parts = email.split('@', 1)
# if len(parts) == 2:
#   username = parts[0]
#   domain = parts[1]
#   print(f"Username: {username}")
#   print(f"Domain: {domain}")
# else:
#   print("Invalid email format")

'''
3. Word Counter

Input:

Python is very easy to learn

Output:

Characters: 30
Words: 6
Vowels: 9
Consonants: 16
'''

# vowel_count = 0
# consonant_count = 0
# sentence = input("Enter: ")
# vowels = "aeiouAEIOU"
# words = sentence.split()
# for char in sentence:
#   if char.isalpha():
#     if char in vowels:
#       vowel_count += 1
#     else:
#       consonant_count += 1
# print(f"Characters: {len(sentence)}")
# print(f"Words: {len(words)}")
# print(f"Vowels: {vowel_count}")
# print(f"Consonants: {consonant_count}")

'''
4. Password Strength Checker

Check whether the password:

- Has at least 8 characters
- Contains uppercase letters
- Contains lowercase letters
- Contains digits
- Contains special characters

Print one of:

Weak
Medium
Strong
'''

# password = input("Enter your password: ")
# special_chars = "!@#$%^&*(),.?\":{}|<>_+-=[];'/\\`~"
# has_length = len(password) >= 8
# has_upper = False
# has_lower = False
# has_digits = False
# has_special = False
# for char in password:
#   if char.isupper():
#     has_upper = True
#   elif char.islower():
#     has_lower = True
#   elif char.isdigit():
#     has_digits = True
#   elif char in special_chars:
#     has_special = True
# criteria_met = sum([has_digits, has_length, has_lower, has_special, has_upper])
# if criteria_met == 5:
#   print("Strong")
# elif criteria_met >= 3:
#   print("Medium")
# else:
#   print("Weak")

'''
5. Mad Libs Game

Ask the user for:

- Name
- Place
- Animal
- Verb
- Food

Generate a funny story using f-strings.
'''

# name = input("Enter your name: ")
# place = input("Enter a place: ")
# animal = input("Enter an animal: ")
# verb = input("Enter a verb: ")
# food = input("Enter a food: ")
# story = f"""
# One day, {name} decided to visit {place}. 
# To everyone's surprise, a giant {animal} was waiting there! 
# The {animal} suddenly started to {verb} wildly. 
# In the chaos, {name} dropped their {food}, which the {animal} immediately ate. 
# It was the strangest day ever!
# """
# print(story)

'''
6. Text Formatter

Input:

   python is AWESOME

Output:

Original:
   python is AWESOME

Trimmed:
python is AWESOME

Upper:
PYTHON IS AWESOME

Lower:
python is awesome

Title:
Python Is Awesome
'''

# message = input("Enter: ")
# print(f"\nTrimmed:\n{message.strip()}\n")
# print(f"Upper:\n{message.strip().upper()}\n")
# print(f"Lower:\n{message.strip().lower()}\n")
# print(f"Title:\n{message.strip().title()}")



# Final Challenge (No Loops)

'''
Profile Card Generator

Ask the user for:

- Name
- Age
- City

Example Output:

==========================
        PROFILE
==========================
Name : Aryan
Age  : 18
City : Delhi
==========================
Hello Aryan! Welcome.
'''

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("\n==========================")
print("        PROFILE           ")
print("==========================")
print(f"Name : {name}")
print(f"Age  : {age}")
print(f"City : {city}")
print("==========================")
print(f"Hello {name}! Welcome.\n")