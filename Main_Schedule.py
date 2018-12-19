import pandas as pd 
 
data = pd.read_csv("nba.csv")

print("Total rows: {}".format(len(data)))
print (list(data))


#Checking if Game(s) entered is valid 
def Game_Range(b):
    for x in data['Date']:
        for y in range (0,(len(data['Date']))):
            if "16/10/2018" in data['Date'][y]:
                return True 
            else:
                print ('Nah')

game = input("Enter a starting game:")
print (Game_Range(game))
