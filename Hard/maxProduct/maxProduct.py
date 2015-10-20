# Given an array of integers. find the contiguous subarray with
# maximum sum.

def maxProduct(arr):
    max_ending_at_i = 1
    min_ending_at_i = 1
    max_so_far = 1

    for i in range(len(arr)):
        if arr[i] > 0:
            max_ending_at_i *= arr[i]
            min_ending_at_i = min(min_ending_at_i * arr[i], 1)
        elif arr[i] == 0:
            max_ending_at_i = 1
            min_ending_at_i = 1
        else:
            temp = max_ending_at_i
            max_ending_at_i = max(min_ending_at_i * arr[i], 1)
            min_ending_at_i = temp * arr[i]

        if max_so_far < max_ending_at_i:
            max_so_far = max_ending_at_i

    return max_so_far
