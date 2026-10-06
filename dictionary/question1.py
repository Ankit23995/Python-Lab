student_info = {"name": "Ram", "age": 22, "grade": "A", "courses": ["DS", "SQL"]}
#1.1
print(student_info["name"])
print(student_info["age"]) #1.2
print(student_info["grade"])
print(student_info["courses"])

print(f"{student_info['name']} is {student_info['age']} years old and got grade {student_info['grade']}.")

print(student_info.get("address"))
print(student_info.get("address", "Not available"))