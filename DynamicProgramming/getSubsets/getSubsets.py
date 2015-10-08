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
        return allSubsets + moreSubsets

# Method 2
# If we look at any given subset of some set, we could think
# of each element in the subset as a "yes" and each element from
# the original set not present in the subset as a "no". So each
# subset is just a sequence of "yes" and "no". We could
# represent each subset, therefore, as a sequence of binary numbers
# from 0 to 2^n (exclusive) where n is the size of set.

def getSubsets2(input_set):
    allSubsets = []
    max_val = 1 << len(input_set)
    for k in range(0, max_val):
        subset = convertFromIntToSet(k, input_set)
        allSubsets.append(subset)
    return allSubsets

def convertFromIntToSet(x, input_set):
    subset = []
    index = 0
    k = x
    while k > 0:
        if k & 1 == 1:
            subset.append(input_set[index])
        index += 1
        k >>= 1
    return subset
