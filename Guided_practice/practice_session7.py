student = {
    "name": "Aryan",
    "age": 22,
    "scores": [88, 92, 79]
}

# Try to:
# 1. Print the student's name

print(student["name"])

# 2. Print their highest score

print(max(student["scores"]))

# 3. Add a new key "grade" with value "A"

student["grade"] = 'A'

# 4. Print all the keys

print(list(student.keys()))

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


students = [
    {"name": "Aryan", "scores": [88, 92, 79]},
    {"name": "Priya", "scores": [95, 87, 91]},
    {"name": "Rahul", "scores": [72, 68, 75]}
]

# Write a function get_average(scores) that takes a list 
# of scores and returns the average

# Then loop through students and print:
# "Aryan: 86.33"
# "Priya: 91.0"
# "Rahul: 71.67"

def get_average(scores:list):
  avg_score = sum(scores) / len(scores)
  return avg_score

for student in students:
  print(f"{student["name"]}: {get_average(student["scores"]):.02f}")