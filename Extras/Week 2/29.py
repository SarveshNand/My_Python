def merge_dicts_sum_values(dict1, dict2):
    """
    Merges two dictionaries. If a key exists in both,
    their values are summed.

    Parameters:
    dict1 (dict): The first dictionary.
    dict2 (dict): The second dictionary.

    Returns:
    dict: A new merged dictionary.
    """
    merged = dict1.copy()  # Start with dict1

    for key, value in dict2.items():
        if key in merged:
            merged[key] += value  # Sum values if key exists
        else:
            merged[key] = value   # Add new key-value pair
    return merged

a = {'apple': 3, 'banana': 2, 'cherry': 5}
b = {'banana': 4, 'cherry': 1, 'date': 7}

result = merge_dicts_sum_values(a, b)
print(result)