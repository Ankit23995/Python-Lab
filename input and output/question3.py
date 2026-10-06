#3.3
feet =input("enter the length in feet:")
feet = float(feet)
Meter = feet * 0.3048
print(f"{feet}in meter is {Meter}")


name = input("Enter your name: ")
print(f"Hello, {name}!")


birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter the current year: "))

age = current_year - birth_year

print(f"You are {age} years old.")



num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2}")


cm = float(input("Enter length in centimeters: "))

meters = cm / 100

print(f"{cm} cm is equal to {meters:.2f} meters.")

