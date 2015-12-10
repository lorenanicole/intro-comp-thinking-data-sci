import pylab, random

def rSquare(measured, estimated):
    """measured: one dimensional array of measured values
       estimate: one dimensional array of predicted values"""
    SEE = ((estimated - measured)**2).sum()
    mMean = measured.sum()/float(len(measured))
    MV = ((mMean - measured)**2).sum()
    return 1 - SEE/MV

def getData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    discardHeader = dataFile.readline()
    for line in dataFile:
        d, m = line.split()
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)

def fitData(fileName):
    masses, distances = getData(fileName)
    masses = pylab.array(masses)
    distances = pylab.array(distances)
    masses = masses*9.81  # convert mass to force (F = mg)

    # Adding coefficient of determination
    totDistances = pylab.array([0]*len(masses))
    for d in distances:
        totDistances = totDistances + pylab.array(distances)

    pylab.plot(masses, distances, 'bo', label = 'Measured points')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('Force (Newtons)')
    pylab.ylabel('Distance (meters)')
    a,b = pylab.polyfit(masses, distances, 1)  # fit y = ax + b
    # use line equation to graph predicted values
    estDistances = a*masses + b
    k = 1/a
    meanDistances = totDistances/float(len(distances))
    pylab.plot(masses, estDistances, label = 'Linear fit, k = '
               + str(round(k, 5)) + str(round(k,5)) + ' R2 = '+ str(round(rSquare(meanDistances, estDistances),4)))
    pylab.legend(loc = 'best')

# fitData('springData.txt')
# pylab.show()

def fitData3(fileName):
    masses, distances = getData(fileName)
    masses = pylab.array(masses[:-6])
    distances = pylab.array(distances[:-6])

    masses = masses*9.81  # convert mass to force (F = mg)

    # Adding coefficient of determination
    totDistances = pylab.array([0]*len(masses))
    for d in distances:
        totDistances = totDistances + pylab.array(distances)

    pylab.plot(masses, distances, 'bo', label = 'Measured points')


    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('Force (Newtons)')
    pylab.ylabel('Distance (meters)')
    a,b = pylab.polyfit(masses, distances, 1)  # fix y = ax + b
    # use line equation to graph predicted values
    estDistances = a*masses + b
    k = 1/a
    meanDistances = totDistances/float(len(distances))

    pylab.plot(masses, estDistances, label = 'Linear fit, k= ' + str(round(k,5)) + ' R2 = '+ str(round(rSquare(meanDistances, estDistances),4)))
    pylab.legend(loc = 'best')


fitData3('springData.txt')
pylab.show()


