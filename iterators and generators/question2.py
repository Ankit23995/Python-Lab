def count_up_to(n):
    for i in range(1, n + 1):
        yield i

numbers = count_up_to(5)

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))



def count_up_to(n):
    for i in range(1, n + 1):
        yield i

for value in count_up_to(5):
    print(value)



def even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i

for value in even_numbers(10):
    print(value)




def square_numbers(n):
    for i in range(1, n + 1):
        yield i ** 2

for value in square_numbers(5):
    print(value)
