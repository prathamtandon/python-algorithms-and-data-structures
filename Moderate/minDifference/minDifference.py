# Given two arrays, find the pair with (one element from each array)
# with minimum positive difference between them.

def minDifference(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    i = 0
    j = 0

    min_diff = float('Inf')
    while i < len(arr1) and j < len(arr2):
        if abs(arr1[i] - arr2[j]) < min_diff:
            min_diff = abs(arr1[i] - arr2[j])

        # move forward the smaller pointer
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return min_diff


