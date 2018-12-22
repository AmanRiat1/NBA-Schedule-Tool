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


    #For loop iterates over game range user enters 
    for game in range (0,7):
        if type(team_sch[game]) == str:
            counter += 1
        else:
            pass

    if counter == 5:
        five.append(teams[index])
    elif counter == 4:
        four.append(teams[index])
    elif counter == 3:
        three.append(teams[index])
    elif counter == 2:
        two.append(teams[index])
    elif counter == 1:
        one.append(teams[index])
    else:
        zero.append(teams[index])
        
        
    index += 1

    
print ("Teams with five games", five)
print ("Teams with four games", four)
print ("Teams with three games", three)
print ("Teams with two games", two)
print ("Teams with one game", one)
print ("Teams that have no games", zero)

        
print (counter)



