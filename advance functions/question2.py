def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))

def product_all(*args):
    product = 1

    for num in args:
        product *= num

    return product

print(product_all(1, 2, 3, 4, 5))


def print_student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_student_info(name="Ram", age=20, course="Python")


def create_profile(**kwargs):
    return kwargs

profile = create_profile(name="Ram", age=20, course="Python")
print(profile)


def show_order(customer_name, *items):
    print("Customer:", customer_name)

    for item in items:
        print("Item:", item)

show_order("Ram", "Pizza", "Burger", "Coke")
