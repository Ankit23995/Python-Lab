#question 1
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

age = 2026 - birth_year

if age >= 18:
    print(f"{name}, You are eligible for voting")
else:
    print(f"{name}, You are not eligible for voting")

#question 2
num_1 = int(input("Enter num_1: "))
num_2 = int(input("Enter num_2: "))

if num_2 == 0:
    print("Cannot divide by zero")
elif num_1 % num_2 == 0:
    print(f"{num_1} is divisible by {num_2}")
else:
    print(f"{num_1} is not divisible by {num_2}")

#question 3
name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = int(input("Enter your salary: "))

if age >= 25 and age <= 50 and salary >= 50000:
    print(f"{name}, You are eligible for loan")
else:
    print(f"{name}, You are not eligible for loan")

#question 4
string = input("Enter a string: ")

if string == string[::-1]:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")

#question 5
balance = 579
amount = int(input("Enter amount to withdraw: "))

if amount <= balance:
    balance = balance - amount
    print(f"{amount} withdrawn successfully. New Balance: {balance}")
else:
    print(f"Insufficient balance. You only have {balance} in your account")
