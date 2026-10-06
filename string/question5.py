file = "report_2026.pdf"
name_extension=file.split(".")
print(name_extension)

my_date="2026-03-05"
date_split =my_date.split("-")
print (date_split)

my_str= "PYTHON"
chara_join=".".join(my_str)
print(chara_join)

laptop_names=["Dell","Hp","Mac"]
laptop_join="-".join(laptop_names)
print(laptop_join)

str_1="Hello,World!"
new_str =str_1.replace("World","Python")
print(new_str)

str_2="2026-03-01"
new_str2=str_2.replace("-","/")
print(new_str2)

str_3="Pineapple"
new_str3=str_3.index("apple")
print(new_str3)

my_name = "Ankit"
my_name = my_name.lower()
count_vowel =my_name.count("a") + my_name.count("e") + my_name.count("i") + my_name.count("o")+ my_name.count("u")  
print(count_vowel)

My_str = "Hello,World!"
count_L=My_str.count("l")
print(count_L)
