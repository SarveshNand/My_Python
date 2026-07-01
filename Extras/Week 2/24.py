def flatten_list(nested_list):
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))  # Recursive call
        else:
            flat.append(item)
    return flat

nested = [1, [2, [3, 4], 5], [6, 7], 8]
print(flatten_list(nested))