from pandas import DataFrame, read_csv
import pandas as pd
import xlrd

#Reading Spreadsheet Data 
file = r'NBA_18_19.xls'
data = pd.read_excel(file)


#Testing Function that will iterate over every team on certains dates
teams = (list(data)[1:31])
index = 0


five = []
four = []
three = []
two = []
one = []
zero = []



while index <= 29:
    counter = 0
    team_sch = (list(data[teams[index]]))
    print (teams[index])

    #For loop iterates over game range user enters 
    for game in range (1):
        if type(team_sch[game]) == str:
            counter += 1
        else:
            pass

    if counter == 1:
        one.append(teams[index])
        
    index += 1
print (one)

        
print (counter)



