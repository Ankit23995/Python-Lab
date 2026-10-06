import pandas as pd

# df =pd.read_csv(r'E:\projects\food_review.csv')
# # print(df)
# # print(df.head(3))
# print(df.tail(2))
# print(df.sample(4)) ## sample data randomly from the overall data in the data set
# filter_condition=df['category']=='Other'
# result = df[filter_condition]
# print(result)
# result.to_csv('Other.csv')
file =pd.read_csv(r'E:\projects\New folder\2022-01-02.csv')
print(file.sample(3))
print(file.dtypes)

#MATPLOTLIB LIBRARY
import matplotlib.pyplot as plt
