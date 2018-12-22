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
                return date_index
            else:
                pass
    

            
#Checking the games played 
def Games_Played(game_start,game_end):

    start = int(game_start)
    end = int(game_end)

    #New list with all NBA Teams
    nba_t = (list(data)[1:31])

    #Lists that will show how many games teams are playing
    five = []
    four = []
    three = []
    two = []
    one = []
    zero = []

    #Variable used as counter to retrieve position of team in list
    team = 0
    
    #Loop iterates over 30 teams
    while team <= 29:
        counter = 0
        team_sch = (list(data[nba_t[team]]))

        #For loop iterates over game range user enters 
        for game in range (start,end+1):
            if type(team_sch[game]) == str:
                counter += 1
            else:
                pass

        if counter == 5:
            five.append(nba_t[team])
        elif counter == 4:
            four.append(nba_t[team])
        elif counter == 3:
            three.append(nba_t[team])
        elif counter == 2:
            two.append(nba_t[team])
        elif counter == 1:
            one.append(nba_t[team])
        else:
            zero.append(nba_t[team])
            
            
        team += 1

        
    print ("Teams with five games:", five)
    print ("Teams with four games:", four)
    print ("Teams with three games:", three)
    print ("Teams with two games:", two)
    print ("Teams with one game:", one)
    print ("Teams that have no games:", zero)


#Main 
game_start = input("Enter the starting date: ")
game_end = input("Enter the ending date: ")

start,end = Game_Checker(game_start),Game_Checker(game_end)


if start and end == True:
    Start_Pos = Game_Position(game_start)
    End_Pos = Game_Position(game_end)
    print (Start_Pos)
    print (End_Pos)
    
    #Counting Games
    Total_games = Games_Played(Start_Pos,End_Pos)
else:
    print ("Invalid Entry")



