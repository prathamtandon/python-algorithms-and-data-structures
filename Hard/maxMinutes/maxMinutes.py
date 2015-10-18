# Given an array of integers, find the largest sum possible such that if
# arr[i] is part of sum, arr[i+1] cannot be part of sum.

# Solution 1: Top-down with memoization.

def maxSum(arr):
    memo = [0]*len(arr)
    return maxSum2(arr,0, memo)

def maxSum2(arr,index, memo):
    if index >= len(arr):
        return 0

    if memo[index] == 0:
        bestWith = arr[index] + maxSum2(arr,index+2,memo)
        bestWithout = maxSum2(arr,index+1,memo)
        memo[index] = max(bestWith, bestWithout)

    return memo[index]

# Solution 2: Bottom-up iterative.

def maxSum3(arr):
    memo = [0]*(len(arr)+2)

    for i in reversed(range(len(arr))):
        bestWith = arr[i] + memo[i+2]
        bestWithout = memo[i+1]
        memo[i] = max(bestWith,bestWithout)

    return memo[0]

# We can actually reduce space complexity to O(1) as we just use two array values at any time. Just replace them with two variables.

def maxSum4(arr):
    oneAway = 0
    twoAway = 0

    for i in reversed(range(len(arr))):
        bestWith = arr[i] + twoAway
        bestWithout = oneAway
        current = max(bestWith, bestWithout)
        twoAway = oneAway
        oneAway = current

    return oneAway
