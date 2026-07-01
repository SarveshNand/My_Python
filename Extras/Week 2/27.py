def find_missing_number(nums):
    """
    Finds the missing number in a list containing numbers from 1 to N.

    Parameters:
    nums (list): A list of integers from 1 to N with one number missing.

    Returns:
    int: The missing number.
    """
    n = len(nums) + 1  # Total count should be N, but one is missing
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

numbers = [1, 2, 4, 5, 6]
print("Missing number:", find_missing_number(numbers))