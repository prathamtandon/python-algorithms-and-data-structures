# Given two arrays, find a pair of elements (one from each array)
# such that by swapping the two elements, both arrays have the same sum.

# Idea is this: say sumA is sum of array A and sumB is sum of array B.
# We are trying to find two elements a and b such that
# sumA - a + b = sumB - b + a or
# a-b = (sumA-sumB)/2
# That is, we are looking for two numbers which have a given difference.
# We can do this in linear time using a hashtable.

def findSwapValues(arr1,arr2):
    target = getTarget(arr1,arr2)
    if target is None:
        return None
    return getDifference(arr1,arr2,target)

def getTarget(arr1,arr2):
    sum1 = sum(arr1)
    sum2 = sum(arr2)

    if ((sum1-sum2)%2) != 0:
        return None
    return abs((sum1-sum2)/2)

def getDifference(arr1,arr2,target):
    contents = set(arr1)
    for val in arr2:
        other = val - target
        if other in contents:
            return (val,other)

    return None

