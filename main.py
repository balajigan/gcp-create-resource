
import pandas as pd
import os

print ("main.py started ...")
print(os.environ)

# read by default sheet of an excel file
dataframe1 = pd.read_excel('sample.xlsx')
 
print(dataframe1)


