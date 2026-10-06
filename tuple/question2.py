salary_tuple = (20000, 25000, 30000)

print("Total number of employees:", len(salary_tuple))
print("Total salary:", sum(salary_tuple))
print("Average salary:", sum(salary_tuple) / len(salary_tuple))
print("Highest salary:", max(salary_tuple))
print("Lowest salary:", min(salary_tuple))
print("Employees with salary 25000:", salary_tuple.count(25000))
print("Index of salary 30000:", salary_tuple.index(30000))

salary_tuple[1] = 35000
