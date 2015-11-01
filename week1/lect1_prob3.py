import pylab

def parseHighLowTemps(file):
	inFile = open(file, "r")
	highTemps, lowTemps = [], []
	for line in inFile.readlines():
		fields = [val.strip("\n") for val in line.split(" ")]
		if not (len(fields) < 3 or not fields[0].isdigit()): 
			highTemps.append(int(fields[1]))
			lowTemps.append(int(fields[2]))
	return lowTemps, highTemps

def producePlot(lowTemps, highTemps):
	# tempDiffs = [highTemps[i] - lowTemps[i] for i in range(0,len(lowTemps))]
	tempDiffs = map(lambda i: highTemps[i] - lowTemps[i], range(len(lowTemps)))
	pylab.figure(1)
	pylab.plot(range(1,32), tempDiffs)
	pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
	pylab.xlabel('Days')
	pylab.ylabel('Temperature Ranges')
	pylab.show()
	pylab.savefig('lect1_prob3')

lowTemps, highTemps = parseHighLowTemps('julyTemps.txt')
producePlot(lowTemps, highTemps)