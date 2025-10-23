# collection = ["great", "good", 21, 34, 55, True, None, "bad", 34, 34]
# no_duplicates = list(set(collection))
# print(no_duplicates)

# collection = ["great", "good", 21, 34, 55, True, None, "bad", 34, 34]
# no_duplicates = list(dict.fromkeys(collection))
# print(no_duplicates)

collection = ["great", "good", 21, 34, 55, True, None, "bad", 34, 34]
no_duplicates = []
for items in collection:
    if items not in no_duplicates:
        no_duplicates.append(items)
print(no_duplicates)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lar_num = max(numbers)
small_num = min(numbers)
print("Largest: ", lar_num)
print("Smallest: ", small_num)


list1 = ["apple", "banana", "mango"]
list2 = ["orange", "grapes", "melon"]
merged_list = list1 + list2
print(sorted(merged_list))