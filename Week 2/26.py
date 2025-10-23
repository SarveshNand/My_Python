def rotate_left(lst, k):
    """
    Rotates a list to the left by k positions.

    Parameters:
    lst (list): The list to rotate.
    k (int): Number of positions to rotate.

    Returns:
    list: The rotated list.
    """
    if not lst:
        return []
    
    k = k % len(lst)  # Handle k > len(lst)
    return lst[k:] + lst[:k]


my_list = [1, 2, 3, 4, 5]
rotated = rotate_left(my_list, 2)
print(rotated)