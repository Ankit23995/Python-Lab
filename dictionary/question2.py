student_info = {"name": "Ram", "age": 22, "grade": "A", "courses": ["DS", "SQL"]}

student_info["grade"] = "A+"
print(student_info)

student_info["level"] = "Beginner"
print(student_info)

student_info["courses"].append("Python")
print(student_info)

student_info.pop("age")
print(student_info)

print(len(student_info))
