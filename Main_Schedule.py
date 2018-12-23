from pandas import DataFrame, read_csv
import pandas as pd
import xlrd

#Reading Spreadsheet Data and creating file object 
file = r'NBA_18_19.xls'
data = pd.read_excel(file)

def Game_Position(game):
    '''
    (str) -> int
    Returns the list position of the date entered 

    >>> Game_Position("12/25")
    70
    '''
    
    for date_index in range (0,(len(data['Date']))):
        if game in data['Date'][date_index]:
            return date_index
        else:
            pass
 
def Games_Played(start, end):
    '''
    (int,int) -> None
    Iterates over the teams in game range to see how many times each team plays
    Game is played if a string is in cell position otherwise it's null
    Prints lists that shows the amount of games teams play
    
    >>> Games_Played(0,7)
    Teams with 4 games: ['Bos', 'Cha', 'Den', 'Gsw', 'Ind',
    'LAC', 'Min', 'NY', 'Orl', 'Phi', 'Sac', 'Tor']

    Teams with 3 games: ['Atl', 'Bkn', 'Chi', 'Cle', 'Dal',
    'Det', 'Hou', 'LAL', 'Mem', 'Mia', 'Mil', 'NO', 'OKC',
    'Pho', 'Por', 'SA', 'Uth', 'Was']

    '''

    #New list with all NBA Teams
    nba_t = (list(data)[1:31])

    #Lists that will show how many games teams are playing
    five = []
    four = []
    three = []
    two = []
    one = []
    zero = []

    #Variable used as counter to retrieve position of team in nba_t list
    team = 0
    
    #Loop iterates over 30 teams
    while team <= 29:
        games_played = 0
        team_sch = (list(data[nba_t[team]]))

        #For loop iterates over game range user enters 
        for game in range (start,end+1):
            if type(team_sch[game]) == str:
                games_played += 1
            else:
                pass

        #Adding teams to lists with the amount of games they play in a week    
        if games_played == 5:
            five.append(nba_t[team])
        elif games_played == 4:
            four.append(nba_t[team])
        elif games_played == 3:
            three.append(nba_t[team])
        elif games_played == 2:
            two.append(nba_t[team])
        elif games_played == 1:
            one.append(nba_t[team])
        else:
            zero.append(nba_t[team])

        #iterating to next team
        team += 1

    #Formatted output to only display lists that have teams in them  
    total_games = [zero,one,two,three,four,five]
    control = 5
    while control != -1:
        if len(total_games[control]) > 0:
            print ("Teams with", control, "games:", total_games[control])
        else:
            pass
        control = control -1 

#Main

print ("Please enter dates in 7 day intervals and in the format of MM/DD")
print ("An example would be from '12/24' to '12/30'")

condition = True 
while condition == True:
    
    start_date = input("Enter the starting date: ")
    end_date = input("Enter the ending date: ")
    print ('')
    
    #A valid date entry must be five characters 
    if len(start_date)and len(end_date) < 5  or len(start_date)and len(end_date) >5:
        print ("Please enter valid dates")
    else:
        condition = False 

try:  
    Start_Pos = Game_Position(start_date)
    End_Pos = Game_Position(end_date)
    
    #Counting Games
    Total_games = Games_Played(Start_Pos,End_Pos)

except:
    print ("Error in date entry, did you make sure to use the MM/DD format?")
