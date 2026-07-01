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

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. A list of all numbers multiplied by 10

mul = [num * 10 for num in numbers]
print(mul)

# 2. A list of only the even numbers

even = [num for num in numbers if num % 2 == 0]
print(even)

# 3. A list of squares of only the odd numbers

sq_odd = [num ** 2 for num in numbers if num % 2 != 0 ]
print(sq_odd)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# You have this raw dataset
students = [
    {"name": "Aryan", "scores": [88, 92, 79], "grade": None},
    {"name": "Priya", "scores": [95, 87, 91], "grade": None},
    {"name": "Rahul", "scores": [55, 48, 60], "grade": None}
]

# Write a function assign_grade(average) that returns:
# "A" if average >= 90
# "B" if average >= 75
# "C" if average >= 60
# "F" otherwise

# Then using your get_average() function from before,
# update each student's grade in the list
# and print only students who passed (grade != "F")

def assign_grade(average):
  if average >= 90:
    return 'A'
  elif average >= 75:
    return 'B'
  elif average >= 60:
    return 'C'
  else:
    return 'F'

def get_average(scores:list):
  avg_score = sum(scores) / len(scores)
  return avg_score

for student in students:
  avg = get_average(student["scores"])
  student["grade"] = assign_grade(avg)
  if student["grade"] != "F":
    print(student)