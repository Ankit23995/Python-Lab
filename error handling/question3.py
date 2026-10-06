import csv
import json


def get_age(birth_year):
    if not isinstance(birth_year, int):
        raise TypeError("Birth year must be an integer")

    current_year = datetime.now().year

    if birth_year > current_year:
        raise ValueError("Birth year cannot be in the future")

    if birth_year < 1900:
        raise ValueError("Birth year is unrealistic")

    return current_year - birth_year


def can_get_adult_pass(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")


def is_leap(year):
    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
        if year % 400 == 0:
            leap = True

    return leap
