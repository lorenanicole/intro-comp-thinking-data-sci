import random
import pylab

def clear(n, clearProb, steps):
	'''
	Not a Monte Carlo simulation as does not take into account randomness. 
	Instead simply uses the clearProb for each timeStep to determine the
	number of molecules that survive.


	n: number of molecules 
	clearProb: probability of molecules being cleared at each timeStep
	steps: number of timeSteps 
	'''
	numRemaining = [n]
	for t in range(steps):
		numRemaining.append(n*((1-clearProb)**t))
	pylab.plot(numRemaining, label = "Exponential decay")

def clearSim(n, clearProb, steps):
	'''
	Same inputs

	Monte Carlos simulation. Unlike above simulation uses random.random() 
	to determine if each molecule will indeed survive at each timeStep. 
	'''
	numRemaining = [n]
	for t in range(steps):
		numLeft = numRemaining[-1]
		for m in range(numRemaining[-1]):
			if random.random() <= clearProb:
				numLeft -= 1
		numRemaining.append(numLeft)
	pylab.plot(numRemaining, 'ro', label = 'Simulation')


clear(1000, 0.01, 500)
clearSim(1000, 0.01, 500)
pylab.xlabel('Number of Steps')
pylab.ylabel('Number of Molecules')
# pylab.semilogy() # Makes y axis logarithmic 
pylab.legend()
pylab.show()

