"""
Problem:

You have a bucket with 3 red balls and 3 green balls. Assume that once you draw a ball out of the bucket, you don't replace it. What is the probability of drawing 4 balls of the same color?

Write a Monte Carlo simulation to solve the above problem.

"""

import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    threeSameColorPicked = 0
    
    for i in range(numTrials):
        if pickBalls(3):
            threeSameColorPicked += 1

    return float(threeSameColorPicked) / numTrials

def pickBalls(numBallsToPick):

    options = ["red", "red", "red", "green", "green", "green"]
    choices = []

    for i in range(numBallsToPick):
        choice = random.choice(options)
        choices.append(choice)
        options.remove(choice)

    return choices == ["red", "red", "red"] or choices == ["green", "green", "green"]

print noReplacementSimulation(1000000)

"""
Probability of pulling three of either color explained:

likelihood of pulling red = 3/6
likelihood of pulling red = 2/5
likelihood of pulling red = 1/4

pulling three of red 3/6 * 2/5 * 1/4 = 1/10
pulling three of green = 1/10

1/10 + 1/10 = 2/20 = 1/10

Therefore P(RRR or GGG) if 1/10 or 0.1

"""

def pickingThreeSameColor(numTrials):
    pickedThree = 0
    for i in range(numTrials):
        if random.random() < 0.1:
            pickedThree += 1
    return float(pickedThree) / numTrials 
