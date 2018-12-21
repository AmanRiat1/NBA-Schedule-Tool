from pandas import DataFrame, read_csv
import pandas as pd
import xlrd

#Reading Spreadsheet Data 
file = r'NBA_18_19.xls'
data = pd.read_excel(file)
print (list(data))
print (len(list(data)))
print (list(data)[30])

#Testing Function that will iterate over every team on certains dates
teams = (list(data)[1:31])

counter = -1
for hey in data[teams[5]]:
    if type(hey) == str:
        counter += 1
    else:
        pass

print (counter)

