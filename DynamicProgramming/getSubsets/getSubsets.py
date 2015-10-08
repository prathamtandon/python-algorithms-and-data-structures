# Return all subsets of a set.

def getSubsets(input_set):
    return getSubsets_helper(input_set, len(input_set))

def getSubsets_helper(input_set, n):
    if n == 0:
        return [[]]
    else:
        allSubsets = getSubsets_helper(input_set, n-1)
        moreSubsets = []
        for subset in allSubsets:
            cloned = list(subset)
            cloned.append(n)
            moreSubsets.append(cloned)
        print str(allSubsets)
        print str(moreSubsets)
        return allSubsets + moreSubsets

