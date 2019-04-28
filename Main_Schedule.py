from pandas import DataFrame, read_csv
import pandas as pd
import xlrd

#Reading spreadsheet data and creating file object 
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

 
        team += 1

    #Formatted output to only display lists that have teams in them  
    total_games = [zero,one,two,three,four,five]
    control = 5
    while control != -1:
        if len(total_games[control]) > 0:
            print ('')
            print ("Teams with", control, "game(s):", total_games[control])
        else:
            pass
        control = control -1

def Week_Games(start,end):
    '''
    (int, int) -> None
    Prints out games days that are light

    >>> Week_Games(76,82)
    Light Game Days:
    Tu-01/01 :  5  games
    Th-01/03 :  3  games
    '''
    #TODO: Add additional output to show which teams play on that day 
    print ("Light Game Days:")
    nba_teams = (list(data)[1:31])


    for date in range (start,end+1):
        teamsInAWeek =[]
        games = 0
        for team in range (0,30):
            current_team = (list(data[nba_teams[team]]))
            if type(current_team[date]) == str:
                    games += 1
                    teamsInAWeek.append(teams(nba_teams[team]))
               
        if games == 0:
            print (data['Date'][date][:2] + ': ' + 'No games!')
        elif games < 14:
            print (data['Date'][date][:2] +': ' + str(games//2), ' games')
            print ('Teams playing this day ',teamsInAWeek)
            print('')


class teams:
    '''
    Object stores team name, start date of back to back, and end date of back to back
    '''
    
    def __init__(self,team,date_start = 0,date_end = 0):
        self.team = team
        self.start = date_start
        self.end = date_end
    
    def __str__(self):
        if (self.start ==0 and self.end ==0):
            return str(self.team)
        return str(self.team) + ': '+ (data['Date'][self.start]) + ' - ' + (data['Date'][self.end])

    def __repr__(self):
        return str(self.team)

    def __eq__(self,other):

        if self.start == other.start and self.end == other.end:
            return True
        else:
            return False 

class back:
    '''
    Displays teams with backs to backs on the same day 
    '''
    def __init__(self,start,end):
        self.start = start
        self.end = end


    def back_teams(self):
        #New list with all NBA Teams
        nba_t = (list(data)[1:31])

        #Counter to retrieve position of team in nba_t list and list of teams with a back to back
        team = 0
        b2b = []

        while team <= 29:
            games_played = 0
            team_sch = (list(data[nba_t[team]]))
  

            for game in range (self.start,self.end+1):
                if type(team_sch[game]) == str and type(team_sch[game+1]) == str:
                    new_team = teams((nba_t[team]),game,game+1)
                    b2b.append(new_team)
                else:
                    pass

            team += 1
        #modified bubble sort to sort teams by date the back to back is played 
        total_teams = len(b2b)
        for i in range(total_teams):
            for j in range (0,total_teams-i-1):
                if (b2b[j]).start > (b2b[j+1]).start:
                    (b2b[j]), (b2b[j+1])= (b2b[j+1]),(b2b[j])       
            
        if len(b2b) > 0:
            #Loops over teams with back to backs to sort and output teams with back to backs on the same days 
            while (len(b2b)) > 0:
                teams_back = []

                #sentinel used to find every team with back to backs on the same day
                b2b_start = b2b[0]
                
                for nba_team in range (len(b2b)):
                    if b2b_start == b2b[nba_team]:
                        teams_back.append(b2b[nba_team])

                #removing teams that have been sorted for a back to back from original list   
                for sorted_team in teams_back:
                    if sorted_team in b2b:
                        b2b.remove(sorted_team)

                date_one = (teams_back[0]).start
                date_two = (teams_back[0]).end 
                print ((data['Date'][date_one][:2]) ,"-", (data['Date'][date_two][:2]) +':', teams_back)
        else:
            print ('No back to backs')

#Main

print ("Please enter dates in a range from 2-7 days. Make sure to use the MM/DD\
 format and the dates are within the NBA season")
print ('')
print ("An example would be from '12/24' to '12/30'")

condition = True 
while condition == True:
    
    start_date = input("Enter the starting date: ")
    end_date = input("Enter the ending date: ")
    
    #A valid date entry must be five characters 
    if len(start_date)and len(end_date) < 5  or len(start_date)and len(end_date) >5:
        print ("Please enter valid dates")
        
    else:
        #try:  
            Start_Pos = Game_Position(start_date)
            End_Pos = Game_Position(end_date)

            if (End_Pos - Start_Pos) > 7 or (End_Pos - Start_Pos) < 1:
                print ('Make sure the dates entered are within a 2-7 day intervals')
                continue 

            else: 
                #Counting Games
                Games_Played(Start_Pos,End_Pos)

                print ('')
                print ('')
                print ('Teams with backs to backs in the week:')
        
                b2b = back(Start_Pos,End_Pos)
                b2b.back_teams()
                print ('')
                print ('')
                Week_Games(Start_Pos, End_Pos)

        #except:
            #print ("Error in date entry, did you make sure to use the MM/DD format?")

    print ('')
    cont = input("Would you like to try another week? Enter anything to continue or enter nothing to stop: ")
    if (len(cont)) > 0:
        continue
    else:
        condition = False




    
