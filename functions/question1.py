def get_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

new_simple=get_simple_interest(5,2,10)
print(int(new_simple))

#question 1.2
def  get_rectangle_area_perimeter(length, width):
    p = 2*(length+width)
    return p
new_p=get_rectangle_area_perimeter(10,10)
print(new_p)

#question 1.3
def is_palindrome(string):
    string == string [::-1]
    return string
new_string=is_palindrome("radar")
print(new_string)

#question 1.4
def count_vowels(string):
    count = 0

    for char in string.lower():
        if char in "aeiou":
            count += 1

    return count

string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))


#question1.5
def get_square_root(num):
    square_root= num **(1/2)
    return square_root

new_square=get_square_root(4)
print(new_square)

