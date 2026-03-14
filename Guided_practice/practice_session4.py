# Write a program that asks the user for a number. If the number is even, print "Even". If odd, print "Odd". If it's greater than 100, also print "Big number!". Use a loop to keep asking until the user types quit.

while True:
  num = input("Enter a number: ")
  if num == 'quit':
    break
  if int(num) > 100:
    print('Big number!')

  if int(num) % 2 == 0:
    print('Even')

  else:
    print('Odd')