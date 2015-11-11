def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if not L:
        return float('NaN')
    tot = 0.0
    newL = map(lambda val: len(val), L)
    mean = sum(newL) / float(len(L))
    for val in newL:
        tot += (val - mean)**2
    return (tot / len(L)) ** 0.5

print stdDevOfLengths(['a', 'z', 'p']) == 0.0
print round(stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples']), 4) == 1.8708 