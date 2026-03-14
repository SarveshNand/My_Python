# Create a program that:
# Asks the user for:
# name
# age
# favourite number

name = input("What's your name? ")
age = int(input("What's your age? "))
fav_num = int(input("What's your favourite number? "))

print(f"Hello {name}")
print(f"Next year you will be {age + 1}")
print(f"Your lucky number doubled is {fav_num * 2}")

# Create a program called:
# Number Guessing Game
# Steps:
# Set a secret number
# secret = 7
# Ask the user to guess the number.
# If guess is wrong → tell them:
# "Too high"
# "Too low"
# Loop until they guess correctly.

secret = 7
guess = int(input("Enter your guess: "))
while secret != guess:
  if guess > secret:
    print("Too high!")
  elif guess < secret:
    print("Too low!")

  guess = int(input("Enter your guess again: "))

print("Correct!")

# Write a program that:
# Asks user for numbers 5 times
# Keeps track of the largest number
# Example:
# Enter number: 3
# Enter number: 9
# Enter number: 4
# Enter number: 1
# Enter number: 7
# Largest number is 9

largest = 0
for i in range(5):
  num = int(input("Enter number: "))
  if num > largest:
    largest =  num
  elif num < largest:
    pass
  elif num == largest:
    pass

print(f"Largest number is {largest}")