from itertools import chain, combinations

def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in xrange(2**N):
        combo = []
        for j in xrange(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    N = len(items)
    for i in xrange(3**N): # for each possibility
    	bag_one, bag_two = [], [] # create two bags
    	for j in xrange(N): # for each item in items
    		if (i / (3 ** j)) % 3 == 1: # if mod one place in first
				bag_one.append(items[j])
 	   		elif (i / (3 ** j)) % 3 == 2: # if mod two place in second
 	   			bag_two.append(items[j])
		yield (bag_one, bag_two) # yield combo


def shortGenP(items):
	for z in chain.from_iterable(combinations(items, r) for r in range(len(items)+1)):
		yield z

for item in shortGenP([1,2,3,4,5,6]):
	print item