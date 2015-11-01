from intDictTests import collision_prob

def bisectionSearchForMaxInsertions(sequence, limit, func, numBuckets):  
    '''
    Bisection search for finding the max number of insertions to be made
    for a given number of buckets to be beneath the (collision) limit.

    sequence: ordered range of values 
    limit: max collision limit represented as a float with two decimal places
    func: function for calculating the collision probability 
    numBuckets: number of buckets for hashing function
    '''
    mid = len(sequence) / 2
    high = len(sequence) - 1
    low = 0 
    if low > high:
        return -1
    if round(func(numBuckets, sequence[mid]), 2) == limit:
        return sequence[mid-1] # If equal to limit want the last highest value under limit.
    if func(numBuckets, sequence[mid]) > limit:
        return bisectionSearchForMaxInsertions(sequence[0:mid], limit, func, numBuckets)
    if func(numBuckets, sequence[mid]) < limit:
        return bisectionSearchForMaxInsertions(sequence[mid+1:], limit, func, numBuckets)


print bisectionSearchForMaxInsertions(range(30,250), 0.99, collision_prob, 365)