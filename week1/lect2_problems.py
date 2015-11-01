'''Problem 2'''

import random
def getEven():
	return random.randrange(0, 99, 2)

# print getEven()

'''Problem 3A'''

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 10 + 2

# print deterministicNumber()

'''Problem 3B'''

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return random.choice(range(10,22,2))

print stochasticNumber()