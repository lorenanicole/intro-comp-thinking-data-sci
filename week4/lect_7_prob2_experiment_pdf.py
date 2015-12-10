'''
Experimenting with probability distribution to model errors when modeling PDF
as the sum of n number of random samples.
'''

import pylab
import random

def testErrorsGaussian(ntrials=10000,npts=100):
    results = [0] * ntrials
    for i in xrange(ntrials):
        s = 0   # sum of random points
        for j in xrange(npts):
            s += random.triangular(-1,1) # Continuous normal probability distribution
        results[i] =s
    # plot results in a histogram
    pylab.hist(results,bins=50)
    pylab.title('Sum of 100 random points -- Triangular PDF (' + ntrials + 'trials)')
    pylab.xlabel('Sum')
    pylab.ylabel('Number of trials')

def testErrorsNormal(ntrials=10000,npts=100):
    '''
    As ntrials increases the variance / standard deviation remains the same (width)
    whereas the mean (height) vastly increases. The probability distribution for the 
    sums approaches a normal distribution.

    The variance depends upon the number of samples taken. The estimate of the distribution 
    function at each point becomes less variable as the number of trials is increased.

    As the number of terms increase (e.g. samples taken), the distribution of the sum 
    approach a normal distribution. This is true even if the underlying distributions are different.
    '''

    results = [0] * ntrials
    for i in xrange(ntrials):
        s = 0   # sum of random points
        for j in xrange(npts):
            s += random.uniform(-1,1) # Discrete Uniform distribution 
        results[i] =s
    # plot results in a histogram
    pylab.hist(results,bins=50)
    pylab.title('Sum of 100 random points -- Uniform PDF (' + ntrials + ' trials)')
    pylab.xlabel('Sum')
    pylab.ylabel('Number of trials')

# testErrorsNormal(1000000)
# pylab.show()