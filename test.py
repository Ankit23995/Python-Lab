import sqlite3


db_path=r'E:\projects\test.db'
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

SQL="SELECT * from employee_info;"
cursor.execute(SQL)
result = cursor.fetchall()
print(result)
cursor.close()
connection.close()

db_path=r'E:\projects\test.db'
connection = sqlite3.connect(db_path)
cursor = connection.cursor()
connection.row_factory =sqlite3.Row # gives result as dictionary instead of list

cursor= connection.cursor()
SQL="select * from sales_info;"
cursor.execute(SQL)
results=cursor.fetchall()

for result in results:
    print(dict(result))


    cursor.close()
connection.close()