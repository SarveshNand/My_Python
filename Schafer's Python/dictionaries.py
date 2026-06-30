# Python Dictionary Practice

# # Level 1: Basics

'''
## 1. Create a Dictionary

Create a dictionary representing a student:

- Name: Alice
- Age: 20
- Course: Python

*Tasks:*
- Print the entire dictionary.
- Print only the course.
'''

# student = {'Name': 'Alice', 'Age': 20, 'course': 'Python'}
# print(student)
# print(student.keys())

'''
## 2. Add a New Key

python
person = {
    "name": "John",
    "age": 25
}


*Task:*

Add:

- city → "New York"

Print the updated dictionary.
'''

# person = {
#     "name": "John",
#     "age": 25
# }
# person['city'] = "New York"
# print(person)

'''
## 3. Update Values

python
car = {
    "brand": "Toyota",
    "year": 2018
}


*Task:*

Update the year to 2024.

Print the dictionary.
'''

# car = {
#     "brand": "Toyota",
#     "year": 2018
# }
# car["year"] = 2024
# print(car)

'''
## 4. Remove a Key

python
employee = {
    "name": "Sara",
    "salary": 50000,
    "department": "HR"
}


*Task:*

Remove the salary key.

Print the updated dictionary.
'''

# employee = {
#     "name": "Sara",
#     "salary": 50000,
#     "department": "HR"
# }
# del employee["salary"]
# print(employee)


# # Level 2: Dictionary Methods

'''
## 5. Using get()

python
student = {
    "name": "Mike",
    "age": 21,
    "grade": "A"
}


*Task:*

Ask the user for a key.

Use .get() to print the value.

If the key doesn't exist, print:


Key not found
'''

# student = {
#     "name": "Mike",
#     "age": 21,
#     "grade": "A"
# }
# user = input("Enter the key: ")
# print(student.get(user, "Key not found"))

'''
## 6. Loop Through a Dictionary

Using the same dictionary:

python
student = {
    "name": "Mike",
    "age": 21,
    "grade": "A"
}


Print:


name -> Mike
age -> 21
grade -> A
'''

# student = {
#     "name": "Mike",
#     "age": 21,
#     "grade": "A"
# }
# for key, value in student.items():
#   print(f"{key} -> {value}")

'''
## 7. Print Only Keys

Using the same dictionary, print:


name
age
grade
'''

# student = {
#     "name": "Mike",
#     "age": 21,
#     "grade": "A"
# }
# for key in student:
#   print(key)

'''
## 8. Print Only Values

Using the same dictionary, print:


Mike
21
A
'''

# student = {
#     "name": "Mike",
#     "age": 21,
#     "grade": "A"
# }
# for value in student:
#   print(student[value])


# # Level 3: Real-Life Problems

'''
## 9. Word Counter

python
sentence = "apple banana apple orange banana apple"


Create a dictionary that counts how many times each word appears.

Expected output:

python
{
    "apple": 3,
    "banana": 2,
    "orange": 1
}
'''

# sentence = "apple banana apple orange banana apple"
# words = sentence.split()
# word_count = {}
# for word in words:
#   if word in word_count:
#     word_count[word] += 1
#   else:
#     word_count[word] = 1
# print(word_count)

'''
## 10. Student Marks

python
marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95
}


*Task:*

Print the student with the highest marks.

*Hint:* max() can help.
'''

# marks = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 95
# }
# print(max(marks))


# # Level 4: Mini Challenges

'''
## 11. Shopping Cart

Create an empty dictionary.

Allow the user to enter:

- Product name
- Quantity

Repeat until the user types:


done


Example:


Enter product: apple
Quantity: 5

Enter product: milk
Quantity: 2

Enter product: done


Expected output:

python
{
    "apple": 5,
    "milk": 2
}
'''

# shopping_list = {}

# while(True):
#   product_name = input("Enter Product name: ")

#   if product_name.lower() == "done":
#     break
  
#   quantity = int(input("Enter Quantity: "))
#   shopping_list[product_name] = quantity
# print(shopping_list)

'''
## 12. Character Frequency

Input:


hello


Expected output:

python
{
    "h": 1,
    "e": 1,
    "l": 2,
    "o": 1
}
'''

# text = input("Input: ")
# char_count = {}
# for char in text:
#   if char in char_count:
#     char_count[char] += 1
#   else:
#     char_count[char] = 1
# print(char_count)


# # Final Challenge: Contacts Manager

'''
Create a contacts dictionary.

Display the following menu repeatedly:


1. Add Contact
2. Search Contact
3. Delete Contact
4. Show All Contacts
5. Exit


Store contacts like this:

python
{
    "Alice": "9876543210",
    "Bob": "9123456789"
}


Your program should allow the user to:

- Add a contact
- Search for a contact
- Delete a contact
- Display all contacts
- Exit the program

Use the following dictionary features:

- in
- get()
- pop()
- items()
'''

contacts = {}
while True:
  print("\n1. Add Contact\n2. Search Contact\n3. Delete Contact\n4. Show All Contacts\n5. Exit")
  choice = int(input("Choose an option (1-5): "))

  if choice ==  1:
    name = input("Enter name: ")
    if name in contacts:
      print("Contact already exists.")
    else:
      number = int(input("Enter number: "))
      contacts[name] = number
      print("Contact added.")

  elif choice == 2:
    name = input("Enter name to search: ")
    
    result = contacts.get(name, "Not found")
    print(f"Number: {result}")

  elif choice == 3:
    name = input("Enter name to delete: ")

    removed = contacts.pop(name, None)
    if removed:
      print("Contact deleted.")
    else:
      print("Contact not found.")

  elif choice == 4:
    for name, number in contacts.items():
      print(f"{name}: {number}")

  elif choice == 5:
    print("Exiting...")
    break
  
  else:
    print("Invalid number.")