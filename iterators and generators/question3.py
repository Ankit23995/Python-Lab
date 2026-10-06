def multiples_of_5():
    for i in range(1, 11):
        yield i * 5

for value in multiples_of_5():
    print(value)



def characters(word):
    for char in word:
        yield char

for value in characters("Python"):
    print(value)



def reverse_numbers(n):
    for i in range(n, 0, -1):
        yield i

for value in reverse_numbers(10):
    print(value)



numbers_list = [i for i in range(1, 1000001)]

def number_generator():
    for i in range(1, 1000001):
        yield i

numbers_generator = number_generator()

print(numbers_list[0])
print(next(numbers_generator))
