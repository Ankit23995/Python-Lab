units = int(input("Enter electricity units consumed: "))

if units <= 20:
    bill = units * 5
elif units <= 50:
    bill = 20 * 5 + (units - 20) * 7
else:
    bill = 20 * 5 + 30 * 7 + (units - 50) * 10

print(f"Total bill: Rs. {bill}")

#question 2
year = int(input("Enter year: "))

if year % 400 == 0:
    print("It is a leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("It is a leap year")
else:
    print("It is not a leap year")

#question 3
amount = float(input("Enter amount: "))

if amount >= 10000:
    discount = amount * 20 / 100
elif amount >= 5000:
    discount = amount * 10 / 100
elif amount >= 2000:
    discount = amount * 5 / 100
else:
    discount = 0

final_amount = amount - discount

print(f"Final amount: Rs. {final_amount}")
