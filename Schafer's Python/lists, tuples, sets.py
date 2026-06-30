# Python Practice: Lists, Tuples, and Sets

# These exercises are designed to help you practice the concepts of *lists, **tuples, and **sets* in Python. Try solving each exercise without looking up the solution.

# # Level 1: Lists

'''
## Exercise 1

Create a list of your five favorite movies.

Tasks:
- Print the whole list.
- Print the first movie.
- Print the last movie.
- Print the length of the list.
'''

# movies = ["The Dark Knight", "Dhurandhar", "The Hangover", "Dune", "Inception"]
# print(movies)
# print(movies[0])
# print(movies[-1])
# print(len(movies))

'''
## Exercise 2

Given:

numbers = [10, 20, 30, 40]

Tasks:
- Add 50.
- Insert 15 at index 1.
- Remove 30.
- Print the final list.

Expected output:

python
[10, 15, 20, 40, 50]
'''

# numbers = [10, 20, 30, 40]
# numbers.append(50)
# numbers.insert(1, 15)
# numbers.remove(30)
# print(numbers)

'''
## Exercise 3

Given:

nums = [7, 3, 9, 1, 5]


Tasks:
- Sort the list.
- Reverse it.
- Find the maximum value.
- Find the minimum value.
'''

# nums = [7, 3, 9, 1, 5]
# print(sorted(nums))
# print(nums[::-1])
# print(max(nums))
# print(min(nums))



# # Level 2: Tuples

'''
## Exercise 4

Create the following tuple:

("John", 25, "Python")


Print each element separately.
'''

# tup = ("John", 25, "Python")
# print(tup[0], tup[1], tup[2])

'''
## Exercise 5

Given:

point = (10, 20)


Unpack it into two variables:

x =
y =


Print:

x = 10
y = 20
'''

# point = (10, 20)
# x = point[0]
# y = point[1]
# print(f"x = {x}\ny = {y}")

'''
## Exercise 6

Run the following code:

colors = ("red", "green", "blue")
colors[0] = "black"


Questions:
- What happens?
- Why does it happen?
'''

# It will give error
# Because tuple is immutable and it doesn't support object assignment


# # Level 3: Sets

'''
## Exercise 7

Create the following set:

{2, 4, 6, 8}


Tasks:
- Add 10.
- Remove 4.
- Print the set.
'''

# set_var = {2, 4, 6, 8}
# set_var.add(10)
# set_var.remove(4)
# print(set_var)

'''
## Exercise 8

Given:

numbers = {1, 2, 2, 3, 3, 4, 4, 5}


Tasks:
- Print the set.
- Explain why duplicate values are missing.
'''

# numbers = {1, 2, 2, 3, 3, 4, 4, 5}
# print(numbers)
# # set only gives us unique values by removing the duplicates while they can be unordered but will always give us unique values

'''
## Exercise 9

Given:

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}


Find:
- Union
- Intersection
- Difference (a - b)
- Symmetric Difference
'''

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))


# # Level 4: Mixed Practice

'''
## Exercise 10

Given:

names = ["Alice", "Bob", "Alice", "John", "Bob", "Mike"]


Without using a loop:
- Remove duplicate names.
- Convert the result back into a list.
'''

# names = ["Alice", "Bob", "Alice", "John", "Bob", "Mike"]
# unique_names = list(set(names))
# print(unique_names)

'''
## Exercise 11

Given:

students = ["A", "B", "C", "D", "E"]


Tasks:
- Convert the list into a tuple.
- Print its type.
'''

# students = ["A", "B", "C", "D", "E"]
# std_tup = tuple(students)
# print(type(std_tup))

'''
## Exercise 12

Given:

nums = [1,2,3,4,5,6,7,8,9,10]


Create:
- A list containing all even numbers.
- A tuple containing all odd numbers.
- A set containing all numbers greater than 5.
'''

# nums = [1,2,3,4,5,6,7,8,9,10]
# even_nums = []
# odd_nums = []
# greater_than_five_nums = []
# for i in nums:
#   if i > 5:
#     greater_than_five_nums.append(i)
#   if i % 2 == 0:
#     even_nums.append(i)
#   else:
#     odd_nums.append(i)
# print(even_nums)
# print(odd_nums)
# print(greater_than_five_nums)


# # Challenge Problems

'''
## Challenge 1

Given:

fruits = ["apple", "banana", "apple", "orange", "banana", "grapes"]


Print:

Unique fruits:
apple
banana
orange
grapes
'''

# fruits = ["apple", "banana", "apple", "orange", "banana", "grapes"]
# unique_fruits = sorted(list(set(fruits)))
# print("Unique fruits:")
# for i in unique_fruits:
#   print(i)

'''
## Challenge 2

Given:

shopping = ["milk", "bread", "eggs"]


Tasks:
1. Ask the user to enter one item.
2. If the item already exists, print:

Already in the list!


3. Otherwise:
   - Add the item.
   - Print the updated list.

'''

# shopping = ["milk", "bread", "eggs"]
# user = input("Enter one item: ")
# if user in shopping:
#   print("Already in the list!")
# else:
#   shopping.append(user)
#   print(shopping)

'''
## Challenge 3

Tasks:
1. Ask the user to enter *5 numbers*.
2. Store them in a list.
3. Print:
   - Largest number
   - Smallest number
   - Average
   - Unique numbers (using a set)
'''

# user_list = []
# for i in range(5):
#   num = int(input("Enter 5 numbers: "))
#   user_list.append(num)

# print("Largest number:", max(user_list))
# print("Smallest number:", min(user_list))
# print("Average:", sum(user_list)/len(user_list))
# print("Unique numbers:", sorted(list(set(user_list))))


# # Mini Project: Student Attendance System

'''
Requirements:

1. Ask the user to enter student names one by one.
2. Stop when the user enters:

done

3. Store all names in a list.
4. Convert the list into a set to find unique students.
5. Print:
   - Total entries
   - Unique students
   - Number of unique students
   - Students in alphabetical order
'''

user_list = []
while(True):
  user = input("Enter student names: ")
  
  if user == "done":
    break
  
  user_list.append(user)

unique_elements = set(user_list)
print("Total entries:", len(user_list))
print("Unique elements:",unique_elements)
print("Number of unique students:",len(unique_elements))
print("Students in alphabetical order:",sorted(unique_elements))