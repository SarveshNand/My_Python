# Create a program that stores student marks.
# Example:
# marks = [78, 85, 90, 66, 88]
# Your program should:
# Print the average marks
# Print the highest marks
# Print the lowest marks

marks = [78, 85, 90, 66, 88]
print(f'Average marks: {sum(marks)/len(marks)}')
print(f'Highest marks: {max(marks)}')
print(f'Lowest marks: {min(marks)}')

# Create a program that:
# Takes 5 numbers from the user
# Stores them in a list
# Prints:
# largest number
# smallest number
# average

number = []
for i in range(5):
  num = int(input('Give a number: '))
  number.append(num)

print(f'Largest: {max(number)}')
print(f'Smallest: {min(number)}')
print(f'Average: {sum(number)/max(number)}')