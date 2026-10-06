#question 2
def get_product_remainder(num_1,num_2):
    product = num_1*num_2
    if num_2 > 0:
        remainder = num_1% num_2
    elif num_2 ==0:
        remainder = "cannot divide by zero"

    return product,remainder

new_prod, rem = get_product_remainder(5,2)
print(new_prod)
print(rem)

#question 3
def calculate_discount(price,discount=10):
    final_price = price - discount
    return final_price

new_final= calculate_discount(500,50)
print(new_final)

#question 1
def greet(name, course="Python"):
    return f"Hello, {name}, Welcome to {course} class."

print(greet("Ram"))
print(greet("Ram", " Data Science"))

#question 4
def get_circle_area(radius, pi=3.14):
    return pi * radius * radius

print(get_circle_area(5))

#question 5
def add_item(item, item_list=None):
    if item_list is None:
        item_list = []

    item_list.append(item)
    return item_list

print(add_item("Apple"))
print(add_item("Mango"))
