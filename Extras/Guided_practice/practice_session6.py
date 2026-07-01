# You have this list
numbers = [4, 17, 2, 93, 45, 8, 101, 56]

# Try to:
# 1. Print the first and last item

print(f"First item: {numbers[0]}")
print(f"Last item: {numbers[-1]}")

# 2. Print only numbers greater than 50

for num in numbers:
  if num > 50:
    print(num)

# 3. Add a new number to the end

numbers.append(99)

# 4. Find how many items are in the list

print(len(numbers))