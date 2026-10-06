file_path =r'E:\projects\New.txt'

content = ''' 
Python is a high-level, interpreted programming language that bridges human logic and machine execution through clean, English-like syntax.
Created by Guido van Rossum and released in 1991, Python prioritizes code readability and developer productivity.
 Guided by the Zen of Python (e.g., "Simple is better than complex"), it uses indentation instead of curly braces to structure code.
   This design reduces maintenance costs and lowers the barrier for beginners.
'''
with open (file_path,'w',encoding='utf-8') as file_obj:
    file_obj.write(content)

new_content ="I will learn error handling"
with open(file_path,'a',encoding='utf-8') as file_obj:
    file_obj.write(new_content)

