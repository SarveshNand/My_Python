def count_frequency(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

lister = ["apple", "banana", "orange", "apple", "banana"]
print(f"Element Frequencies: {count_frequency(lister)}")