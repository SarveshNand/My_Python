def count_words(sentence):
    words = sentence.split()
    return len(words)

print(count_words("Hello how are you buddy"))


user_input = input("Enter something to save to the file: ")
with open('user_input.text', 'w') as f:
    f.write(user_input)


import json
with open('data.json', 'r') as f:
    data = json.load(f)
print(data)


dictionary = {"name" : "rahul",
              "age" : 45,
              "b'day" : 22/2/1999,
              "gender" : "male"}
convert_dict = json.dumps(dictionary)
print(convert_dict)


jsonwa = '{ "name":"John", "age":30, "city":"New York"}'
convert_json = json.dumps(jsonwa)
print(convert_json)