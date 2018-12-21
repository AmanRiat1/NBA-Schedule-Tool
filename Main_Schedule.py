from pandas import DataFrame, read_csv
import pandas as pd
import xlrd


#List Data relvant info from 1 - 30 

#Reading Spreadsheet Data 
file = r'NBA_18_19.xls'
data = pd.read_excel(file)
print (list(data))

#Checking if Game(s) entered is valid 
def Game_Checker(game):

    for date in data['Date']:
        for date_index in range (0,(len(data['Date']))):
            if game in data['Date'][date_index]:
                return True
            else:
                pass

#Returns the date's position in the list           
def Game_Position(game):

    for date in data['Date']:
        for date_index in range (0,(len(data['Date']))):
            if game in data['Date'][date_index]:
                return game
            else:
                pass
    

            
#Checking the games played 
def Games_Played(game_start,game_end):

    #New list with all NBA Teams
    nba_t = (list(data)[1:31])

    #TODO: Fix loop so it iterates over 30 teams     
    counter = -1
    for team in data[nba_t[5]]:
        if type(team) == str:
            counter += 1
        else:
            pass

    print (counter)



#Main 
game_start = input("Enter the starting date: ")
game_end = input("Enter the ending date: ")

start,end = Game_Checker(game_start),Game_Checker(game_end)


if start and end == True:
    Start_Pos = Game_Position(game_start)
    End_Pos = Game_Position(game_end)
    
    #Counting Games
    Total_games = Games_Played(Start_Pos,End_Pos)
else:
    print ("Invalid Entry")



