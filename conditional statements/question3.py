age = int(input("Enter your age: "))
citizenship = input("Are you a citizen? ")

if age >= 18 and citizenship.lower() == "yes":
    print("You can vote")
else:
    print("You cannot vote")


username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")


marks = int(input("Enter your marks: "))
attendance = int(input("Enter attendance percentage: "))

if marks >= 40 and attendance >= 75:
    print("You are eligible for exam")
else:
    print("You are not eligible for exam")


number = int(input("Enter a number: "))

if number >= 10 and number <= 50:
    print("The number is between 10 and 50")
else:
    print("The number is not between 10 and 50")


day = input("Enter day: ")

if day.lower() == "saturday" or day.lower() == "sunday":
    print("It is weekend")
else:
    print("It is weekday")
