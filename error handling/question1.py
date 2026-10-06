def count_lowercase(text):
    try:
        return sum(1 for char in text if char.islower())
    except TypeError:
        return "Input must be a string"

print(count_lowercase("Hello Python"))
print(count_lowercase(123))


def density(mass, volume):
    try:
        return mass / volume
    except ZeroDivisionError:
        return "Volume cannot be zero"
    except TypeError:
        return "Mass and volume must be numbers"

print(density(10, 2))
print(density(10, 0))
print(density("10", 2))



def get_name(data):
    try:
        return data["name"]
    except KeyError:
        return "Key 'name' not found"

print(get_name({"name": "Rabindra", "age": 30}))
print(get_name({"age": 30}))



def get_third_element(items):
    try:
        return items[2]
    except IndexError:
        return "List has fewer than three elements"

print(get_third_element([10, 20, 30]))
print(get_third_element([10, 20]))
