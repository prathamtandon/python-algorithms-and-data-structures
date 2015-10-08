# A magic index in an array A[1...n-1] is an index i such that A[i] = i.
# Given a sorted array of distinct integers, write a method to find
# a magic index, if one exists, in array.
# FOLLOW UP: What if values are not distinct

def magicIndex(arr):
    return magicIndex_helper(arr, 0, len(arr)-1)

def magicIndex_helper(arr, low, high):
    if low > high:
        return -1
    mid = (low + high) / 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return magicIndex_helper(arr, low, mid-1)
    else:
        return magicIndex_helper(arr, mid+1, high)

# For second part, when the elements in the array can repeat, we
# cannot decide simply to go left or right by comparing a[mid] and
# mid. Take below example:
# -10 -5 2 2 2 3 4 7 9 12 13
#   0  1 2 3 4 5 6 7 8 9  10
# Now a[mid] = 3 and mid = 5. So as per above function, we will have
# to search the right subarray. However, we would also have to search
# the left subarray. However, should we search the entire left ? No!
# since, arr[5] = 3, arr[4] cannot be 4, since 4 cannot appear before
# 3 in sorted order. However, arr[3] can be 3. So we have to search
# from start of left till index 'midValue' (3 in above case)
# We can generalize this logic as:
# If arr[mid] != mid:
# 1) search left half from start till min(mid-1, arr[mid])
# 2) search right half from max(mid+1,arr[max]) to end

def magicIndex_Repition(arr):
    return magicIndex_Repition_helper(arr, 0, len(arr)-1)

def magicIndex_Repition_helper(arr, low, high):
    if low > high:
        return -1
    mid = (low + high) / 2
    midVal = arr[mid]
    if midVal == mid:
        return mid
    # Search left
    left = min(mid-1, midVal)
    left_result = magicIndex_Repition_helper(arr, low, left)
    if left_result >= 0:
        return left_result
    # Search right
    right = max(mid+1, midVal)
    right_result = magicIndex_Repition_helper(arr, right, high)
    return right_result
