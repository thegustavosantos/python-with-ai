import pandas as pd

df = pd.read_csv("data/students.csv")

print(df)        #  mostrar todo o dataframe 
print(df.head())  # mostrar os 5 primeiros
print(df.head(2))  # mostrar os 2 primeiros

print(df.tail())  # mostrar os 5 últimos
print(df.tail(2))  # mostrar os 2 últimos