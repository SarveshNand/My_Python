def key_exists(dictionary, key):
    return key in dictionary

my_dict = {
    "name": "Joy",
    "age": 12,
    "city": "Toronto"
}

key_to_check = input("Enter the key to check: ")

if key_exists(my_dict, key_to_check):
    print(f"Key {key_to_check} exists with value: {my_dict[key_to_check]}")
else:
    print(f"Key {key_to_check} does not exist in the dictionary.")