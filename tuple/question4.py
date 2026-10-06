employee_names = ("Rabindra", "Bob", "Charlie")
employee_salaries = (20000, 25000, 30000)

print( len(employee_names))
print(sum(employee_salaries))
print( sum(employee_salaries) / len(employee_salaries))
highest_salary= max(employee_salaries)
print(highest_salary)
lowest_salary =  min(employee_salaries)
print(lowest_salary)

highest_index = employee_salaries.index(max(employee_salaries))
lowest_index = employee_salaries.index(min(employee_salaries))

print( employee_names[highest_index])
print(employee_names[lowest_index])

print(employee_salaries.count(25000))

employee_data = list(zip(employee_names, employee_salaries))
print( employee_data)
