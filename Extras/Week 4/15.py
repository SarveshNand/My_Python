def merge_two_dict(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

dict1 = {
    "name": "Luffy",
    "age": 20,
    "power type": "devil fruit",
}

dict2 = {
    "name": "Naruto",
    "age": 21,
    "power type": "chakra"
}

print(merge_two_dict(dict1, dict2))