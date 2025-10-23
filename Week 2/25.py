def second_highest(numbers):
    unique_numbers = list(set(numbers))  # Remove duplicates
    if len(unique_numbers) < 2:
        return None  # Not enough unique values
    unique_numbers.sort(reverse=True)  # Sort descending
    return unique_numbers[1]

nums = [4, 1, 7, 3, 7, 9, 9]
result = second_highest(nums)

if result is not None:
    print("Second highest number:", result)
else:
    print("List doesn't have enough unique values.")