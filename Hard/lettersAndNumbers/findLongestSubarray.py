# Given an array filled with letters and numbers, find the longest
# subarray with an equal number of letters and numbers.

# The main idea is to track the difference between the number of letters
# and numbers at each index i for a subarray arr[0...i].
# Say we observe a difference d at index i. Now, suppose we encounter
# the same difference d again at some other index j. What does this mean ?
# It means that we have added the same number of letters and numbers
# from index i through index j. So, the longest subarray with equal
# number of letters and numbers will be the one with max(j-i). Note
# that the actual subarray will start from index i+1 and end at index j.

def findLongestSubarray(arr):
    # compute deltas between count of numbers and count of letters.
    deltas = computeDeltaArray(arr)

    # find pair in deltas with matching difference and largest span.
    match = findLongestMatch(deltas)

    return arr[match[0]+1:match[1]]

def countDeltaArray(arr):
    deltas = [0]*len(arr)
    delta = 0

    for i in range(len(arr)):
        if arr[i].isdigit():
            delta -= 1
        else:
            delta += 1
        deltas[i] = delta

    return deltas

def findLongestMatch(deltas):
    hashmap = {}
    hashmap[0] = -1
    max_span = (0,0)
    for i in range(len(deltas)):
        if deltas[i] in hashmap:
            other = hashmap[deltas[i]]
            if i - other > max_span[1] - max_span[0]:
                max_span = (other,i)
        else:
            hashmap[deltas[i]] = i

    return max_span
