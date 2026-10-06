squares = [x ** 2 for x in range(10)]
print(squares)


even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)


countries = ["Nepal", "usa", "UK"]

uppercase_countries = {country.upper() for country in countries}
print(uppercase_countries)


squares = {x: x ** 2 for x in range(1, 6)}
print(squares)


marks = {"Ram": 80, "Sita": 45, "Hari": 30}

result = {name: "Pass" if mark >= 40 else "Fail" for name, mark in marks.items()}
print(result)
