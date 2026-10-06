numbers = [1, 4, 5, 7, 8, 12]
evaluated_data = []

for num in numbers:
    if num == 4:
        continue
    if num == 8:
        break
    if num % 2 != 0:
        evaluated_data.append(num * 2)
    else:
        evaluated_data.append(num * 3)

print(evaluated_data)

numbers = [1, 2, 3, 4, 5, 6, 7]

for num in numbers:
    if num == 5:
        break
    print(num)

numbers = [1, -3, 4, -2, 7, -8]

for num in numbers:
    if num < 0:
        continue
    print(num)
