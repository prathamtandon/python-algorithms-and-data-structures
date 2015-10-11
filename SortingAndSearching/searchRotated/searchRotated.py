# Given a sorted array, which has been rotated an unknown number of
# times, search for a value in the array.

# The idea is to compare array[mid] with array[left], if array[low]
# < array[mid], it means the left half is normally sorted. So we can
# just compare x with array[low] and array[mid] to decide whether
# to search in left half or right half. Similarly, if array[low] >
# array[mid], it means that the right half is normally ordered and we
# can compare x again to search in right or left.

# A special case is with duplicate values, where we may have to search
# in both halves.

def searchRotated(arr, low, high, x):
    mid = (low + high)/2
    if arr[mid] == x:
        return mid
    if low > high:
        return -1

    if arr[low] < arr[mid]:
        if arr[low] <= x < arr[mid]:
            return searchRotated(arr, low, mid-1, x)
        else:
            return searchRotated(arr, mid+1, high, x)

    elif arr[low] > arr[mid]:
        if arr[mid] < x <= arr[high]:
            return searchRotated(arr, mid+1, high, x)
        else:
            return searchRotated(arr, low, mid-1, x)

    else:
        if arr[mid] != arr[high]: # Right half contains unique values
            return searchRotated(arr, mid+1, high, x)
        else:
            result = searchRotated(arr, low, mid-1, x)
            if result == -1:
                result = searchRotated(arr, mid+1, high, x)
            return result
