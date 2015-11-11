import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def stdDev(X):
    mean = sum(X) / float(len(X)) # mean which is mu
    tot = 0.0
    for x in X:
        tot += (x - mean) **2 # summation of each trial - mean squared
    return (tot/len(X))**0.5 

def wordVowelFreq(word):
    charList = list(word)
    vowelCount = 0.0
    for char in charList:
        if char.lower() in 'aeiou':
            vowelCount += 1
    # print "word: ", word, " vowelCount: ", vowelCount
    return vowelCount / len(word)

def labelPlot(size, mean, sd):
    pylab.title('Vowel Proportion of ' + str(size) + ' Words ')
    pylab.xlabel('Fraction of Vowels')
    pylab.ylabel('Number of Words')
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    pylab.text(xmin + (xmax-xmin)*0.02, (ymax-ymin)/2,
               'Mean = ' + str(round(mean, 4))
               + '\nSD = ' + str(round(sd, 4)))

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    fracVowels = []
    for i in range(len(wordList)):
        fracVowels.append(wordVowelFreq(wordList[i]))
    mean = sum(fracVowels)/len(wordList)
    sd = stdDev(fracVowels)
    pylab.hist(fracVowels, bins = numBins) 
    xmin,xmax = pylab.xlim()
    ymin,ymax = pylab.ylim()
    labelPlot(len(wordList), mean, sd)
    pylab.show()


if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)


