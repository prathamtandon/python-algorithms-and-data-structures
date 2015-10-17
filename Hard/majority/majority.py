# Given an array of positive integers, return a "majority" element
# which takes more than half the space in the array. Return -1
# if no majority element found. You should do this in O(n) time and
# O(1) extra space.

def findMajorityElement(arr):
    candidate = getCandidate(arr)
    return candidate if validate(arr,candidate) is True else -1

def getCandidate(arr):
    count = 0
    majority = 0
    for val in arr:
        if count == 0:
            majority = val
        if val == majority:
            count += 1
        else:
            count -= 1

    return majority

def validate(arr, majority):
    count = 0
    for val in arr:
        if val == majority:
            count += 1

    return count > len(arr)/2
