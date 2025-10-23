def remove_none_values(lst):
    return [item for item in lst if item is not None]

my_list = [1, None, 2, None, 3, 4, None, 5]
clean_list = remove_none_values(my_list)
print(clean_list)