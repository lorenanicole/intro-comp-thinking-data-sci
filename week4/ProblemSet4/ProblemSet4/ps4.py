# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials, condition=75):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    trialResults = {trialNum: 0 for trialNum in range(numTrials)}
    for trial in range(numTrials):
        viruses = [ResistantVirus(0.1, 0.05, {'guttagonol': False}, 0.005) for x in range(100)]
        treatedPatient = TreatedPatient(viruses, 1000)
        for timeStep in range(0,condition+150):
            treatedPatient.update()
            if timeStep == condition:
                treatedPatient.addPrescription('guttagonol')
        print str(trial) + " Completed"
        trialResults[trial] = treatedPatient.update()
    print trialResults
    pylab.hist(trialResults.values(), bins=20)
    pylab.title("Final Resistant Population - Prescription Given After " + str(condition) + " Time Steps for " + str(numTrials) + " Trials")
    pylab.xlabel("Final Total Virus Population")
    pylab.ylabel("Number of Trials")
    pylab.legend(loc='best')
    pylab.show()


simulationDelayedTreatment(2000, 300)


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO

# 300 
# 175
# 75
#  0 time steps before administering the drug
#  TreatedPatient(viruses, maxPop):
# patient = 



