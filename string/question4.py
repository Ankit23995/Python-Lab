str_1="Hello"
str_2="134"
str_3="##abc123##"
str_4=""

print(str_1.isalpha())

print(str_1.isdigit())

print(str_2.isalnum())

print(str_4.isspace())

print(str_3.startswith("abc"))

print(str_3.startswith("123"))

print(str_1.startswith("He") and str_1.endswith("lo"))


print(str_3.strip("#"))

print(str_3.lstrip("#"))

print(str_3.rstrip("#"))
