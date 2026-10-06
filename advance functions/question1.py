cube = lambda x: x ** 3

print(cube(5))


my_num = [1, 4, 7, 9, 12, 18]

result = list(filter(lambda x: x % 3 == 0, my_num))

print(result)


my_num = [1, 4, 7]

result = list(map(lambda x: x ** 3, my_num))

print(result)


from functools import reduce

my_num = [1, 5, 7, 9]

result = reduce(lambda x, y: x * y, my_num)

print(result)


names = ["ram", "hari", "sita"]

result = list(map(lambda x: x.upper(), names))

print(result)
