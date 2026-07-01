create_dict = {"name" : "Sarvesh",
               "age": 20,
               "profession": "Student"}
print(create_dict)


create_dict["profession"] = "Ai Engineer"
create_dict.pop("age")
print(create_dict)


new_dict = {"Name" : "Sarvesh",
            "Age" : 20,
            "Phone" : "Poco",
            "Laptop" : "HP",
            "TV" : "Croma",
            "Read Books" : True}
for keys, values in new_dict.items():
    print(f"Keys: {keys}, Values: {values}")