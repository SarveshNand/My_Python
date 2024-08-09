# Merging

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = dict1 | dict2
print(merged)   # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

dict3 = {'a': 1, 'b': 2}
dict4 = {'b': 3, 'c': 4}
merged = dict3 | dict4
print(merged)   # Output: {'a': 1, 'b': 3, 'c': 4}