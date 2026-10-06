x=10

def find_x():
    x = 5

print(x)

#question3.2
def greet(name):
    """This function greets the user with their name."""
    return f"Hello, {name}!"

print(greet.__doc__)
print(greet("Ram"))

#question3.3
def my_function():
    x = 10  

my_function()

print(x)

#question3.4
counter = 0

def increment():
    global counter
    counter += 1

print(counter)
increment()
print(counter)

#question3.5
def outer_function():
    count = 0
    
    def inner_function():
        nonlocal count
        count += 1
        return count
        
    return inner_function

counter = outer_function()
print(counter())
