# name = input("Enter Name: ")
# for i in range(1, 11):
#     print(name)


# string = input("Enter the string: ")
# reverse_string = string[::-1]
# print(reverse_string)


# texts = input("Enter something: ")
# vowel = "aeiouAEIOU"
# count_vowel = "".join(items for items in texts if items in vowel)
# print(count_vowel)


lister = ["hello", "bye", "moshi moshi", "sayonara", 55, True, None, 75.7, "moshi moshi"]
frequency = {}
for item in lister:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print(frequency)