age = int(input("Enter your age: "))
salary = int(input("Enter your salary: "))

if age >= 25 and age <= 50:
    if salary >= 50000:
        print("You are eligible for loan")
    else:
        print("You are not eligible for loan")
else:
    print("You are not eligible for loan")


username = input("Enter username: ")
password = input("Enter password: ")

if username == "ankit":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Invalid username")


marks = int(input("Enter your marks: "))

if marks >= 0 and marks <= 100:
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Invalid marks")


