numbers = [1, -3, 0, 2, 0, 7, 10, 8, -1]

def get_data(l, r, x):
    total = 0

    for i in range(l, r + 1):
        if numbers[i] == 0:
            total += x
        else:
            total += numbers[i]

    return total

print(get_data(2, 6, 5))
