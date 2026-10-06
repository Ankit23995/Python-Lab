college_1 = {
    "python": {"duration": 3, "type": "basic"},
    "java": {"duration": 4, "type": "medium"}
}

college_2 = {
    "multimedia": {"duration": 2, "type": "basic"},
    "javascript": {"duration": 5, "type": "advanced"}
}

print(college_1["python"])
print(college_1["python"]["duration"])
print(college_1["java"]["type"])

college_1["python"]["type"] = "advanced"
print(college_1)
college_1.update(college_2)

print(college_1) 

