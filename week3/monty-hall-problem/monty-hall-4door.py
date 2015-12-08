'''
instead of 3 doors, 1 car, and 2 goats, instead there are 
4 doors, 2 cars and 2 goats.

Probability explained:
Originally 2/4 chance winning
4 doors total - Monty picks one with goat
3/4 chance winning

'''

import pylab
import random

def montyChoose(guessDoor, prizeDoors):
    for door in [1,2,3,4]: 
        if door != guessDoor and door != prizeDoors[0] and door != prizeDoors[1]: 
            return door

def playerStickChoice(montyDoor, choiceOne): 
    return choiceOne

def playerSwitchChoice(montyDoor, choiceOne): 
    prizeDoorChoices = [1,2,3,4] 
    prizeDoorChoices.remove(montyDoor) 
    prizeDoorChoices.remove(choiceOne) 
    return random.choice(prizeDoorChoices) 

def simMontyHall(numTrials, montyChooseFcn, playerChooseFcn):
    '''
    Simulation controlling for how both Monty would chose the door after the
    first guess is made and how the player would chose after Monty selects a 
    door. 

    To compare results of staying with original door vs. switching use a 
    different playerChooseFcn.
    '''
    win, lose = (0, 0)
    prizeDoorChoices = [1,2,3,4]
    guessChoices = [1,2,3,4]
    for t in range(numTrials):
        prizeDoorOne = random.choice(prizeDoorChoices)
        prizeDoorChoices.remove(prizeDoorOne)
        prizeDoorTwo = random.choice(prizeDoorChoices)
        prizeDoors = [prizeDoorOne, prizeDoorTwo]
        choiceOne = random.choice(guessChoices)
        montyDoor = montyChooseFcn(choiceOne, prizeDoors)
        finalDoor = playerChooseFcn(montyDoor, choiceOne)
        if finalDoor in prizeDoors:
            win += 1
        else:
            lose += 1
        prizeDoorChoices = [1,2,3,4]
    return (win, lose)
 
simResults = simMontyHall(100000, montyChoose, playerSwitchChoice) 

def displayMHSim(simResults, title):
    stickWins, switchWins = simResults
    pylab.pie([stickWins, switchWins],
              colors = ['r', 'c'],
              labels = ['stick', 'change'],
              autopct = '%.2f%%')
    pylab.title(title)

print simResults

# displayMHSim(simResults, 'Monty Chooses a Door')

