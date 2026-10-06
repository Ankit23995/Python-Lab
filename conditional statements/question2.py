#question 1
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Your grade is A")
elif marks >= 80:
    print("Your grade is B")
elif marks >= 70:
    print("Your grade is C")
elif marks >= 60:
    print("Your grade is D")
else:
    print("Your grade is F")

#question 2
birth_year = int(input("Enter your birth year: "))
age = 2026 - birth_year

if age <= 12:
    print("You are a child")
elif age <= 19:
    print("You are a teenager")
elif age <= 59:
    print("You are an adult")
else:
    print("You are a senior")

#question 3
side_1 = int(input("Enter side 1: "))
side_2 = int(input("Enter side 2: "))
side_3 = int(input("Enter side 3: "))

if side_1 == side_2 and side_2 == side_3:
    print("This is an equilateral triangle")
elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
    print("This is an isosceles triangle")
else:
    print("This is a scalene triangle")

#question 4
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

if num_1 > num_2:
    print(f"The largest number is {num_1}")
elif num_2 > num_1:
    print(f"The largest number is {num_2}")
else:
    print(f"Both numbers are equal: {num_1}")

hour = int(input("Enter hour: "))

#question5
if hour >= 5 and hour <= 11:
    print("Good Morning")
elif hour >= 12 and hour <= 16:
    print("Good Afternoon")
elif hour >= 17 and hour <= 20:
    print("Good Evening")
elif hour >= 21 and hour <= 23:
    print("Good Night")
elif hour >= 0 and hour <= 4:
    print("Good Night")
else:
    print("Invalid time")
