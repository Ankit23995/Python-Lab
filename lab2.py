import csv
import json
file_path=r'E:\projects\New folder\2022-01-02.csv'

with open(file_path,'r',encoding='utf-8')as file_obj:
    csv_reader=csv.reader(file_obj)
    data = list(csv_reader)

  