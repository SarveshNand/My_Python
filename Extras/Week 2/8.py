def merger_dict(dict1, dict2):
    merged = {**dict1, **dict2}
    return merged

dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}

print(merger_dict(dict_a, dict_b))