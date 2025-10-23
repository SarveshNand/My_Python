import json

dictionary = {"name": "Sarvesh",
              "age": 20,
              "laptop": "HP",
              "phone": True
              }
convert_dict = json.dumps(dictionary)
print(convert_dict)


jsony = '{ "name":"John", "age":30, "city":"New York"}'
convert_json = json.loads(jsony)
print(convert_json)


with open('data.json', 'w') as f:
    json.dump(jsony, f)