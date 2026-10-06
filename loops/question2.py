num_tuple = (1, 4, 7, 12, 20)

even_numbers = []
total = 0

for num in num_tuple:
    if num % 2 == 0:
        even_numbers.append(num)
        total += num

print(even_numbers)
print(total)


num_set = {1, 3, 5, 7, 9}

odd_numbers = []
product = 1

for num in num_set:
    if num % 2 != 0:
        odd_numbers.append(num)
        product *= num

print(odd_numbers)
print(product)


numbers = [10, 25, 7, 40, 15, 30]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest:", second_largest)


fruits = ["Apple", "banana", "Avocado", "mango", "orange"]

new_list = []

for fruit in fruits:
    if fruit.startswith("a") or fruit.startswith("A"):
        new_list.append(fruit.upper())
    else:
        new_list.append(fruit.lower())

print(new_list)


fruits = ["Apple", "banana", "Avocado", "mango", "orange"]

new_list = [
    fruit.upper() if fruit.startswith("a") or fruit.startswith("A") else fruit.lower()
    for fruit in fruits
]

print(new_list)


for i in range(1, 6):
    print("*" * i)
