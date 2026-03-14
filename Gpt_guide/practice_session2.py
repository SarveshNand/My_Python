# Conditionals and loops practice

# Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

n = []
for i in range(1500, 2701):
  if i % 7 == 0 and i % 5 == 0:
    n.append(str(i))
print(','.join(n))

# Write a Python program to count the number of even and odd numbers in a series of numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = 0
odd = 0
for num in numbers:
  if num % 2 == 0:
    even += 1
  else:
    odd += 1
print(f'Number of even numbers: {even}')
print(f'Number of odd numbers: {odd}')

# Write a Python program that prints each item and its corresponding type from the following list.

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for data in datalist:
  print(f'The data {data} have the type {type(data)}')

# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

for i in range(7):
  if i == 3 or i == 6:
    continue
  else:
    print(i)

# Write a Python program to get the Fibonacci series between 0 and 50.

x, y = 0, 1
while y < 50:
  print(y)
  x, y = y, x + y

# Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".

for i in range(51):
  if i % 3 == 0:
    print('Fizz')
  elif i % 5 == 0:
    print('Buzz')
  elif i % 3 == 0 and i % 5 == 0:
    print('FizzBuzz')
  else:
    print(i)

# Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.

for i in range(100, 401):
  if i % 2 == 0 and i < 400:
    print(i, end=',')
  elif i == 400:
    print(i)
  else:
    pass

# Write a Python program to calculate a dog's age in dog years.
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

h_age = int(input('Input a dog\'s age in human years: '))
if h_age < 0:
  print('Age must be a positive number.')
  exit()
elif h_age <= 2:
  d_age = h_age * 10.5
else:
  d_age = 21 + (h_age - 2) * 4

print('The dog\'s age in dog\'s year is', d_age)