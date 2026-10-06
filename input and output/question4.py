Mass =float(input("enter the mass of the cube:"))
length =float(input("enter the length of the cube:"))
volume = length**3
density = Mass/ volume
print(f"density of the cube is {density:.3f}")



name = input("Enter your name: ")
price = float(input("Enter the price of the pen: "))

print(f"{name} bought a pen for Rs. {price:.2f}.")


year = int(input("Enter current year: "))
month = int(input("Enter current month: "))
day = int(input("Enter current day: "))

print(f"Today's Date: {year:04d}-{month:02d}-{day:02d}")



name = input("Enter your name: ")

mark1 = float(input("Enter marks in subject 1: "))
mark2 = float(input("Enter marks in subject 2: "))
mark3 = float(input("Enter marks in subject 3: "))

average = (mark1 + mark2 + mark3) / 3

print(f"{name} scored {average:.1f}% in exam.")

filename = input("Enter a file name (file.ext): ")

extension = filename.split(".")[-1]

print(f"File extension: {extension}")