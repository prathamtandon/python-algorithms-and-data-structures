# Given an array of positive and negative integers, find the maximum
# contiguous sum in the array.

def contiguousSum(arr):
    sum_val = 0
    max_val = 0

    for i in range(len(arr)):
        sum_val += arr[i]
        if sum_val > max_val:
            max_val = sum_val
        elif sum_val < 0:
            sum_val = 0

    return max_val
