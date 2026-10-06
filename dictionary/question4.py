student_info = {"name": "Ram", "age": 22, "grade": "A"}

copied_info = student_info.copy()

copied_info["name"] = "Bob"
copied_info["grade"] = "B"

print(student_info)
print(copied_info)

new_info = student_info

new_info["age"] = 25

print(student_info)
print(new_info)