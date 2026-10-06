for i in range(1, 11):
    print(i)


i = 1

while i <= 10:
    print(i)
    i += 1


for i in range(2, 21, 2):
    print(i)


i = 1

while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1


num = 7
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(factorial)


num = 7
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(factorial)
