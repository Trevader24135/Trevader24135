from multiprocessing import Pool
from random import randint
import sys
sys.path.append(r"C:\Users\Trevor\Documents\python")
from dice import roll

import time
start_time = time.time()

def check(i):
    if player[i] > 39:
        player[i] -= 40
    t = player[i]
    #landed on go to jail
    if t == 30:
        player[i] = 10
        rolled[0] = 0
        rolled[1] = 0
    #if the player landed on community chest, chose their fate!
    if player[i] == 2 or player[i] == 17 or player[i] == 33:
        drawn = randint(1,17)
        if drawn == 1:
            player[i] = 0
        if drawn == 2:
            player[i] = 10
            #going to jail would stop double rolls
            rolled[0] = 0
            rolled[1] = 0
    
    #if the player landed on chance, chose their fate! BLOOD FOR THE BLOOD GODS-, er nothing.
    if player[i] == 7 or player[i] == 22 or player[i] == 36:
        drawn = randint(1,17)
        #advance to go
        if drawn == 1:
            player[i] = 0
        #advance to illinois avenue
        elif drawn == 2:
            player[i] = 24

        #advance to St. Charles Place
        elif drawn == 3:
            player[i] = 11

        #advance to the nearest utility
        elif drawn == 4:
            if player[i] == 7:
                player[i] = 12
            elif player[i] == 22 or player[i] == 36:
                player[i] = 28
                
        #advance to the nearest railroad (There are two of these)
        elif drawn == 5 or drawn == 6:
            if player[i] == 7:
                player[i] = 15
            elif player[i] == 22:
                player[i] = 25
            elif player[i] == 36:
                player[i] = 5
        #go back three spaces
        elif drawn == 7:
            player[i] -= 3

        #go to jail
        elif drawn == 8:
            player[i] = 10
            #going to jail would stop double rolls
            rolled[0] = 0
            rolled[1] = 0
            
        #take a trip to the reading railroad
        elif drawn == 9:
            player[i] = 5

        #take a walk on the boardwalk
        elif drawn == 10:
            player[i] = 39
#start all players at 0 (start)
player = [0,0,0,0]

#start dice at 0
rolled = [0,0]

#main function
def game(naught):
    #start all tile scores at 0
    scores = []
    for i in range(40):
        scores.append(0)

    #100 turns per game
    for turn in range(1,101):
        
        #4 player per turn
        for i in range(4):

            #roll the dice and move the player.
            rolled = roll(2,6)
            player[i] += rolled[0]

            #check if the player landed on anything special
            check(i)

            #add points to the tile the player rests on
            scores[player[i]] += 1

            #decide if the player rolled a double and gets to roll again
            if rolled[1] == 1:
                rolled = roll(2,6)
                player[i] += rolled[0]
                check(i)
                scores[player[i]] += 1

            #decide if the player rolled a double a third time and goes to jail
            if rolled[1] == 1:
                #set the player's tile to jail, and adds the point
                player[i] == 10
                scores[player[i]] += 1
    return(scores)
#how many games to run
games =   1000000
tpr =     1000
workers = 10
#file to backup results to


#estimated time to run
print("estimated time (minutes) required:" + str((.00105*games)/60))

scores = []
score = []
for i in range(40):
    score.append(0)
average = []
#not sure why, but this line below is absolutely required for multithreading.
#my theory is that it prevents child-threads from creating more children. (incest?)
if __name__ == '__main__':
    #sets the number of workers (Pool(X)) x = # of workers
    
    pool = Pool(workers)

    #makes the children run the main game function as many times as game is.
    for i in range(int(games/tpr)):
        print(str(((i*tpr)/games)*100)+"%")
        scores = pool.map(game,range(tpr))
        
        #adds all the scores together then divides them. it's simply getting the average.
        scores = scores + [score]
        score = [sum(x) for x in zip(*scores)]

        #open the backup file and save the current results
        file = open('results.txt', 'w')
        if i != 0:
            file.write(str([ x / (i*tpr) for x in score]) + " | ran " + str((i+2)*tpr) + " times!")
        
    #when the child finishes, close it'self and rejoin
    pool.close()
    pool.join()

    #print 100% for the sake of completing
    print("100.0%")

    #close the file and re open it to save over the old copy
    file.close()
    file = open('results.txt', 'w')

    #prints finishing time
    print("%s seconds" % (time.time() - start_time))
    
    #lists out all the property names and their final scores
    average = [ x / games for x in score]
    names = ["start|", "Mediteranean Avenue|", "Brown Community Chest|", "Baltic Avenue|", "Income Tax|", "Reading Railroad|", "Oriental Avenue|", "Light Blue Chance|", "Vermont Avenue|", "Connecticut Avenue|", "Jail|", "St Charles Place|", "Electric Company|", "States Avenue|", "Virginia Avenue|", "Pennsylvania Railroad|", "St James Place|", "Orange Community Chest|", "Tennessee Avenue|", "New York Avenue|", "Free Parking|", "Kentucky Avenue|", "Red Chance|", "Indiana Avenue|", "Illinois Avenue|", "B & O Railroad|", "Atlantic Avenue|", "Ventnor Avenue|", "Water Works|", "Marvin Gardens|", "Go to jail|", "Pacific Avenue|", "North Carolina Avenue|", "Green Community Chest|", "Pennsylvania Avenue|", "Short Line RailRoad|", "Blue Chance|", "Park Place|", "Luxury Tax|", "Boardwalk|"]
    for i in range(40):
        print(names[i] + str(average[i]))
    #backup the final results
    file.write(str(average) + " | completed successfully!")
    file.close()
    #done!
