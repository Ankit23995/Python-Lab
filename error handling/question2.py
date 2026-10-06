def can_get_adult_pass(age):

    if type(age) != int:
        raise TypeError("age must be in integer")
    if age <= 0:
        raise ValueError("age can only be positive number nor can it be zero")
    if age > 100:
        raise ValueError("It is near impossible for humans to live that long.")
    if age > 18:
        return True
    else:
        return False


your_age = can_get_adult_pass(18)
print(your_age)

from datetime import datetime


def get_age(birth_year):
    if not isinstance(birth_year, int):
        raise TypeError("Birth year must be an integer")

    current_year = datetime.now().year

    if birth_year > current_year:
        raise ValueError("Birth year cannot be in the future")

    if birth_year < 1900:
        raise ValueError("What are u?Immortal?")

    return current_year - birth_year


print(get_age(2000))


def calculate_rectangle_area(length, width):
    if not isinstance(length, (int, float)) or isinstance(length, bool):
        raise TypeError("Length must be a number")

    if not isinstance(width, (int, float)) or isinstance(width, bool):
        raise TypeError("Width must be a number")

    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be greater than 0")

    return length * width


print(calculate_rectangle_area(10, 5))
