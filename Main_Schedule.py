from pandas import DataFrame, read_csv
import pandas as pd
import xlrd

#Reading Spreadsheet Data 
file = r'NBA_18_19.xls'
data = pd.read_excel(file)
print (list(data))

#Checking if Game(s) entered is valid 
def Game_Range(game_start):
    for date in data['Date']:
        for date_index in range (0,(len(data['Date']))):
            if game_start in data['Date'][date_index]:
                return True, date_index
            else:
                pass

            
#Checking the games played 
def Games_Played(game_start,game_end):
    counter = 0
    print (type(data['Atl'][1]))
    if (type(data['Atl'][1])) == str:
        counter += 1
    print (counter)

    
game = input("Enter a starting game: ")
print (Game_Range(game))


