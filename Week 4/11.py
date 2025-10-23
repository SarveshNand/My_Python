import re

def sum_of_numbers_in_string(input_string):
    numbers = re.findall(r'\d+', input_string)
    numbers = [int(num) for num in numbers]
    return sum(numbers)

input_string = "I have 2 apples, 3 bananas, and 10 oranges."
result = sum_of_numbers_in_string(input_string)
print(f"The sum of numbers in the string is: {result}")