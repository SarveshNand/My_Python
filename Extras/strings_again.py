# string = input("Enter something: ")
# reversed_string = string[::-1]
# print(reversed_string)

# item_code = "TX12400X00"
# size_code = item_code[-3:]
# print(size_code)

# character = "shakalaka boom boom"
# count_characters = character.count("boom")
# print(count_characters)

text = input("Write something: ")
vowels = "aeiouAEIOU"
removed_vowel = "".join(ch for ch in text if ch not in vowels)
print(removed_vowel)