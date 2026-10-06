import json
import csv

data = {
    "9843": {"name": "Rabindra", "age": 30, "course": "Python"},
    "9844": {"name": "Hari", "age": 25, "course": "Java"},
    "9845": {"name": "Sita", "age": 22, "course": "Python"},
    "9846": {"name": "Gita", "age": 28, "course": "Java"},
    "9847": {"name": "Ram", "age": 24, "course": "Python"}
}

with open("info.json", "w") as file:
    json.dump(data, file, indent=4)




with open("info.json", "r") as file:
    data = json.load(file)

records = []

for phone, details in data.items():
    record = {
        "phone": phone,
        "name": details["name"],
        "age": details["age"],
        "course": details["course"]
    }
    records.append(record)

with open("info.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["phone", "name", "age", "course"])
    writer.writeheader()
    writer.writerows(records)



  

with open("E:\projects\New folder\election_result.json", "r") as file:
    data = json.load(file)

winner = max(data, key=lambda x: x["votes"])

print(winner["name"])
print(winner["party"])
print(winner["votes"])




with open("E:\projects\New folder\election_result.json", "r") as file:
    data = json.load(file)

total_votes = sum(candidate["votes"] for candidate in data)
average_votes = total_votes / len(data)

print(total_votes)
print(average_votes)



with open("E:\projects\New folder\election_result.json", "r") as file:
    data = json.load(file)

with open("E:\projects\New folder\election_result.json", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)