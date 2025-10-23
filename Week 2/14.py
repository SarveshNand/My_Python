def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

common = find_common_elements(list_a, list_b)
print("Common elements:", common)