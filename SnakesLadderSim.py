import random
import csv

map = [0,38,2,3,14,5,6,7,8,31,10,
         11,12,13,14,15,16,7,18,19,20,
         42,22,23,24,25,26,27,84,29,30,
         31,32,33,34,35,36,37,38,39,40,
         41,42,43,44,45,46,47,48,49,50,
         67,52,53,34,55,56,57,58,59,60,
         61,19,63,60,65,66,67,68,69,70,
         91,72,73,74,75,76,77,78,79,100,
         81,82,83,84,85,86,24,88,89,90,
         91,92,73,94,75,96,97,79,99,100]

numberOfPlays = 10000
games = []

def getDieRoll():
    return random.randint(1,6)

def playGame():
    currPos = 0
    thisPlayMovement = []
    thisPlayRolls = []
    snakesLadders = ""
    thisPlayMovement.append(currPos)
    while(currPos!=100):
        d = getDieRoll()
        currPos += d
        if(currPos<=100):
            t = currPos
            currPos = map[t]
            if(currPos>t):
                snakesLadders += "L-"+str(t) + " "
            if(currPos<t):
                snakesLadders += "S-"+str(t) + " "    
        else:
            t = currPos-100
            currPos = map[t]
            if(currPos>t):
                snakesLadders += "L-"+str(t) + " "
            if(currPos<t):
                snakesLadders += "S-"+str(t) + " " 
        thisPlayMovement.append(currPos)
        thisPlayRolls.append(d)
    thisGame = []
    thisGame.append(len(thisPlayRolls))
    thisGame.append(thisPlayMovement)
    thisGame.append(thisPlayRolls)
    thisGame.append(snakesLadders)
    games.append(thisGame)

def main():
    for i in range(numberOfPlays):
        playGame()
    
    saveGames()
    
def saveGames():
    saveGames = games.copy()
    headings = ['Game Length','Player Movement','Die Rolls', 'Snakes and Ladders']
    saveGames.insert(0,headings)
    with open('snakesAndLadders.csv', 'w', newline='') as gameFile:
        writer = csv.writer(gameFile)
        writer.writerows(saveGames)

main()