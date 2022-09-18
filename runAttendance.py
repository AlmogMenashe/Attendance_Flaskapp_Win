#!/usr/bin/bash

from ast import Str
import pandas as pd

path = "attendance.csv"

#read a file        
df = pd.read_csv(path)

#Create a new df
df2 = df[['names','average']]
df2 = df2.sort_values('average').reset_index(drop=True)
df2 = df2.sort_index(ascending=False)
df2 = df2.reset_index(drop=True)
print(df2)
df3 = df2
df3["average"] = df3["average"].replace({' %':' '}, regex=True).astype("float")
df3["average"] = round(df3['average'],2).astype("str") +' %'
print(df3)
print("********** Copy to a new data **********")
