def unique_elements_only_in_one(list1, list2):
    """
    Returns elements that are present in only one of the two lists.

    Parameters:
    list1 (list): First list.
    list2 (list): Second list.

    Returns:
    list: A list of elements unique to each list.
    """
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.symmetric_difference(set2))

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

result = unique_elements_only_in_one(a, b)
print("Unique elements in only one list:", result)