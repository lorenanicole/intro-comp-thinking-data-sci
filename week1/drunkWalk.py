import pylab

class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
        
    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Field(object):
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


import random

class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name

class UsualDrunk(Drunk): #Abstract class used to create subtypes!
    def takeStep(self):
        stepChoices = [(0.0,1.0), (0.0,-1,0), (1.0,0.0), (-1.0,0.0)] # Models one step in each of the cardinal directions
        choice = random.choice(stepChoices)
        return choice[0], choice[1]

def walk(field, drunk, numSteps):
	start = field.getLoc(drunk)
	for s in range(numSteps):
		field.moveDrunk(drunk)
	return (start.distFrom(field.getLoc(drunk)))

def simWalks(numSteps, numTrials):
	homer = UsualDrunk('Homer')
	origin = Location(0,0)
	distances = []
	for t in range(numTrials):
		f = Field()
		f.addDrunk(homer, origin)
		distances.append(walk(f, homer, numSteps))
	return distances 

def drunkTestP(numTrials = 50):
	stepsTaken =  [10,100,1000,10000,100000]
	meanDistances = []
	for numSteps in stepsTaken:
		distances = simWalks(numSteps, numTrials)
		meanDistances.append(sum(distances)/len(distances))
	pylab.plot(stepsTaken, meanDistances)
	pylab.title('Mean Distance from Origin')
	pylab.xlabel('Steps Taken')
	pylab.ylabel('Steps from Origin')
	pylab.show()

drunkTestP(50)
