import csv

data = [
    ["Name", "Age", "Grade"],
    ["Ram", 18, "A"],
    ["Sita", 19, "B"],
    ["Hari", 18, "A+"],
    ["Gita", 20, "B+"],
    ["John", 19, "A"]
]

with open("std_1.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)




data = [
    {"Name": "Ram", "Age": 18, "Grade": "A"},
    {"Name": "Sita", "Age": 19, "Grade": "B"},
    {"Name": "Hari", "Age": 18, "Grade": "A+"},
    {"Name": "Gita", "Age": 20, "Grade": "B+"},
    {"Name": "John", "Age": 19, "Grade": "A"}
]

with open("std_2.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Age", "Grade"])
    writer.writeheader()
    writer.writerows(data)





with open("E:\projects\New folder\2022-01-03.csv", "r", newline="") as file:
    reader = csv.reader(file)
    records = list(reader)

print(records)




with open("E:\projects\New folder\2022-01-03.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    records = list(reader)

print(records)
