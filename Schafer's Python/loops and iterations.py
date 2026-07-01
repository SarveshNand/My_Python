# Python Loops & Iterations Practice

# Level 1 – Basic `for` Loops

## 1. Print numbers from 1 to 10.

# for i in range(1, 11):
#   print(i)

## 2. Print numbers from 10 to 1.

# for i in range(10, 0, -1):
#   print(i)

## 3. Print all even numbers from 1 to 20.

# for num in range(1, 21):
#   if num % 2 == 0:
#     print(num)

## 4. Print all odd numbers from 1 to 20.

# for num in range(1, 21):
#   if num % 2 != 0:
#     print(num)

'''
## 5. Print each character of the string:

word = "Python"
'''

# word = "Python"
# for char in word:
#   print(char)

'''
## 6. Print this pattern:

*
**
***
****
*****
'''

# for i in range(1, 6):
#   for j in range(i):
#     print("*", end="")
#   print()


# Level 2 – Basic `while` Loops

## 7. Print numbers from 1 to 10 using a `while` loop.

# num = 1
# while num <= 10:
#   print(num)
#   num += 1

## 8. Print numbers until 50 that are divisible by 5.

# num = 0
# while num <= 50:
#   if num % 5 == 0:
#     print(num)
#   num += 1

## 9. Ask the user to enter a number repeatedly until they enter `0`.

# num = int(input("Enter a number: "))
# while num != 0:
#   num = int(input("Enter a number: "))
#   if num == 0:
#     break

'''
## 10. Countdown from 10 to 1, then print:

Blast off!
'''

# countdown = 10
# while countdown >= 1:
#   print(countdown)
#   countdown -= 1
# print("Blast off!")


# Level 3 – Loops + `if`

'''
## 11. Print numbers from 1 to 30.

- If a number is divisible by 3, print `"Fizz"` instead.
- Otherwise, print the number.
'''

# for num in range(1, 31):
#   if num % 3 == 0:
#     print("Fizz")
#   else:
#     print(num)

## 12. Print numbers from 1 to 50 that are divisible by both 3 and 5.

# for num in range(1, 51):
#   if (num % 3 == 0) and (num % 5 == 0):
#     print(num)

'''
## 13. Count how many vowels are in:

text = "corey schafer"
'''

# text = "corey schafer"
# vowels = "aeiou"
# vowel_counter = 0
# for ch in text:
#   if ch in vowels:
#     vowel_counter += 1
# print(vowel_counter)

'''
## 14. Print all uppercase letters from:

text = "PyThOn Is FuN"
'''

# text = "PyThOn Is FuN"
# for ch in text:
#   if ch.isupper():
#     print(ch)


# Level 4 – Nested Loops

'''
## 15. Print:

1 2 3
1 2 3
1 2 3

'''

# for i in range(1, 4):
#   for j in range(1, 4):
#     print(j, end=" ")
#   print()

'''
## 16. Print the multiplication table from **1 to 5** in this format:

1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25
'''

# for i in range(1, 6):
#   for j in range(1, 6):
#     print(i*j, end="\t")
#   print()

'''
## 17. Print this pattern:

*****
*****
*****
*****
'''

# for i in range(1, 5):
#   for j in range(1, 6):
#     print("*", end="")
#   print()

'''
## 18. Print:

1
22
333
4444
55555
'''

# for i in range(1, 6):
#   for j in range(i):
#     print(i, end="")
#   print()


# Level 5 – `break` and `continue`

## 19. Print numbers from **1 to 20**, but skip multiples of **3**.

# for i in range(1, 21):
#   if i % 3 == 0:
#     continue
#   print(i)

## 20. Print numbers from **1 to 20**, but stop the loop when the number reaches **13** (do **not** print `13`).

# for i in range(1, 21):
#   if i == 13:
#     break
#   print(i)

'''
## 21. Ask the user for a password until they enter:

python123

Then print:

Access granted
'''

# while True:
#   password = input("Enter the password: ")
#   if password == "python123":
#     break
# print("Access granted")


# Level 6 – Challenge

'''
## 22. Guess the Number

Hardcode a secret number:

secret = 7

Keep asking the user for guesses until they enter the correct number.

Then print:

Correct!
'''

# secret = 7
# while True:
#   guess = int(input("Enter your guess: "))
#   if guess == secret:
#     break
# print("Correct!")

'''
## 23. Reverse a string using a loop.

> **Constraint:** Do **not** use slicing (`[::-1]`).
'''

# string = input("Enter a string: ")
# reversed_string = ""
# for char in string:
#   reversed_string = char + reversed_string
# print(reversed_string)

'''
## 24. Count how many digits are in an integer entered by the user.

> *Bonus:* Make your solution work for negative numbers as well.
'''

# integer = int(input("Enter the integer: "))
# digits = 0
# num = abs(integer)
# if num == 0:
#   digits = 1
# else:
#   while num > 0:
#     digits += 1
#     num //= 10
# print(digits)

'''
## 25. Print this pyramid:
    *
   ***
  *****
 *******
*********
'''

# rows = 5
# for i in range(rows):
#   for j in range(rows - i - 1):
#     print(" ", end="")
#   for j in range(2 * i + 1):
#     print("*", end="")
#   print()


# Bonus Challenges

'''
Try solving these without using lists.

- Print all prime numbers from **1 to 100**.
- Calculate the factorial of a number.
- Find the largest digit in a number.
- Sum all even numbers from **1 to n**.
- Print the first **n** terms of the Fibonacci sequence.
'''

# for num in range(2, 101):
#   for i in range(2, num):
#     if num % i == 0:
#       break
#   else:
#     print(num, end=" ")

# num = int(input("Enter a number: "))
# fact = 1
# if num < 0:
#   print("Factorial does not exist for negative numbers.")
# elif num == 0:
#   print("The factorial of 0 is 1")
# else:
#   for i in range(1, num + 1):
#     fact *= i
# print(f"The factorial of {num} is {fact}")

# num = int(input("Enter number: "))
# n = abs(num)
# largest = 0
# if n == 0:
#   largest = 0
# else:
#   while n > 0:
#     digit = n % 10
#     if digit > largest:
#       largest = digit
#     n //= 10
# print(f"The largest digit in {num} is: {largest}")

# summ = 0
# num = int(input("Enter number: "))
# n = abs(num)
# if n == 0:
#   summ = 0
# else:
#   while n > 0:
#     digit = n % 10
#     summ += digit
#     n //= 10
# print(f"The sum of the digits in {num} is: {summ}")

num = int(input("Enter terms: "))
first = 0
second = 1
for i in range(num):
  print(first, end=" ")
  first, second = second, first + second