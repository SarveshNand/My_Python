# Python Practice: Conditionals & Booleans

# # Level 1: Basic if Statements

'''
## Exercise 1: Voting Eligibility

Ask the user for their age.

- If the age is *18 or older*, print:
  
  You can vote.
  
- Otherwise, print:
  
  You cannot vote yet.
'''

# age = int(input("Enter your age: "))
# if age >= 18:
#   print("You can vote.")
# else:
#   print("You cannot vote yet.")

'''
## Exercise 2: Positive, Negative, or Zero

Ask the user to enter a number.

Print:

- Positive if the number is greater than 0.
- Negative if the number is less than 0.
- Zero if the number is exactly 0.
'''

# number = int(input("Enter a number: "))
# if number > 0:
#   print("Positive")
# elif number < 0:
#   print("Negative")
# else:
#   print("Zero")

'''
## Exercise 3: Password Checker

Ask the user to enter a password.

- If it matches:
  
  python123
  
  print:
  
  Access granted
  

- Otherwise print:
  
  Access denied
'''

# password = input("Enter password: ")
# if password == "python123":
#   print("Access granted")
# else:
#   print("Access denied")


# # Level 2: Using if, elif, and else

'''
## Exercise 4: Grade Calculator

Ask the user for their score (0–100).

Print the corresponding grade:

| Score | Grade |
|--------|-------|
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| Below 60 | F |
'''

# score = int(input("Enter your score: "))
# if score >= 90 and score <= 100:
#   print("A")
# elif score >= 80 and score < 90:
#   print("B")
# elif score >= 70 and score < 80:
#   print("C")
# elif score >= 60 and score < 70:
#   print("D")
# else:
#   print("F")

'''
## Exercise 5: Temperature Checker

Ask the user for the current temperature.

Print:

- Above 30:
  
  It's hot.
  

- Between 20 and 30 (inclusive):
  
  Nice weather.
  

- Below 20:
  
  It's cold.
'''

# temp = int(input("Enter current temperature: "))
# if temp > 30:
#   print("It's hot.")
# elif temp >= 20 and temp <= 30:
#   print("Nice weather.")
# else:
#   print("It's cold.")


# # Level 3: Boolean Operators

'''
## Exercise 6: Club Entry

Ask the user for:

- Age
- Whether they have an ID (yes or no)

Allow entry only if:

- Age is *18 or older*
- *AND*
- They have an ID.
'''

# age = int(input("Enter your age: "))
# id = input("You have id?(yes or no): ").lower()
# if age >= 18 and id == "yes":
#   print("You can enter.")
# else:
#   print("You cannot enter.")

'''
## Exercise 7: Going Outside

Ask:

- Is it raining? (yes or no)
- Do you have an umbrella? (yes or no)

Print:


Go outside.


if:

- It is *not raining*
- *OR*
- The user has an umbrella.

Otherwise print:


Stay inside.
'''

# rain = input("Is it raining?(yes or no): ").lower()
# umbrella = input("Do you have an umbrella?(yes or no): ").lower()
# if rain == "no" and umbrella == "yes":
#   print("Go outside.")
# else:
#   print("Stay inside.")

'''
## Exercise 8: Login System

Ask the user for:

- Username
- Password

Correct credentials:

- Username:
  
  admin
  
- Password:
  
  python
  

Only print:


Login successful


if *both* are correct.

Otherwise print:


Login failed
'''

# username = input("Enter username: ")
# password = input("Enter password: ")
# if username == "admin" and password == "python":
#   print("Login successful")
# else:
#   print("Login failed")


# # Level 4: Comparison Operators

'''
Ask the user for two numbers.

Print the result of each comparison:

- First > Second
- First < Second
- First == Second
- First != Second
- First >= Second
- First <= Second
'''

# first = int(input("Enter first number: "))
# second = int(input("Enter second number: "))
# print(first > second)
# print(first < second)
# print(first == second)
# print(first != second)
# print(first >= second)
# print(first <= second)


# # Level 5: Mini Challenges

'''
## Exercise 9: Even or Odd

Ask for a number.

Print whether it is:

- Even
- Odd
'''

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#   print("Even")
# else:
#   print("Odd")

'''
## Exercise 10: Leap Year Checker

Ask the user for a year.

Determine whether it is a leap year.
'''

# year = int(input("Enter year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#   print("Leap year")
# else:
#   print("Not a leap year")

'''
## Exercise 11: Largest of Three Numbers

Ask the user for three numbers.

Print the largest one.
'''

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# if num1 > num2 and num1 > num3:
#   print(f"Largest: {num1}")
# elif num2 > num1 and num2 > num3:
#   print(f"Largest: {num2}")
# elif num3 > num1 and num3 > num1:
#   print(f"Largest: {num3}")
# else:
#   print("All are same")

'''
## Exercise 12: Vowel Checker

Ask the user for a single character.

Print whether it is a vowel.
'''

# vowel = "aeiou"
# char = input("Enter a single character: ")
# if char in vowel:
#   print("Vowel")
# else:
#   print("Not a vowel")

'''
## Exercise 13: Century Checker

Ask the user for a year.

Print whether it belongs to the *21st century*.
'''

# year = int(input("Enter a year: "))
# if year >= 2001 and year <= 2100:
#   print("This year belongs to the 21st century.")
# else:
#   print("This year does not belongs to the 21st century.")

'''
## Exercise 14: Student Discount

Ask the user for their age.

The user qualifies if:

- Age is less than *18*
- *OR*
- Age is *60 or older*

Print whether they qualify.
'''

# age = int(input("Enter your age: "))
# if age < 18 or age >= 60:
#   print("You are qualified to apply for student discount.")
# else:
#   print("You are not qualified for the student discount")


# # Final Challenge

'''
Write a program that asks for:

- Username
- Password
- Age

Rules:

- Username must be:
  
  admin
  
- Password must be:
  
  python123
  
- Age must be at least *18*

Output:

If everything is correct:


Welcome!


If the username or password is incorrect:


Invalid credentials


If the credentials are correct but the age is under 18:


You must be 18 or older
'''

username = input("Enter your username: ")
password = input("Enter your password: ")
age = int(input("Enter your age: "))
if username != "admin" or password != "python123":
  print("Invalid credentials")
  if age >= 18:
    print("Welcome!")
  else:
    print("You must be 18 or older")
else:
  print("Invalid credentials")