students = {
    "S001": {
        "name": "Alice",
        "age": 20,
        "grades": {"Math": 85, "Science": 90, "English": 78}
    },
    "S002": {
        "name": "Bob",
        "age": 22,
        "grades": {"Math": 75, "Science": 78, "English": 79}
    },
    "S003": {
        "name": "Charlie",
        "age": 21,
        "grades": {"Math": 81, "Science": 87, "English": 93}
    }
}

print(students["S001"]["grades"]["Science"])

for student_id, record in students.items():
    print(f"{student_id}: {record['name']}")