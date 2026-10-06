student_record = {
    "9843": {"course": "Python", "name": "Ram", "present": False},
    "9844": {"course": "Java", "name": "Shyam", "present": True},
    "9845": {"course": "Python", "name": "Sita", "present": True}
}

for student in student_record.values():
    if student["course"] == "Python" and student["present"] == False:
        print(student["name"])


numbers = [1, 4, 7, 3, 8, 12]

for num in numbers:
    if num == 10:
        print("10 found")
        break
else:
    print("10 not found")
