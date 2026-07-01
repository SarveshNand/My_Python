def create_dict(n):
    for key,value in n.items():
        print(f"{key}: {value}")

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(create_dict(person))