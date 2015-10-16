# Given an array of integers, find indices m and n such that if you
# sorted elements m through n, the entire array would be sorted.
# Minimize n-m.

def findUnsortedSequence(arr):
    end_left = findEndOfLeft(arr)
    if end_left >= len(arr)-1:
        return

    start_right = findStartOfRight(arr)

    max_index = end_left
    min_index = start_right

    for i in range(end_left+1,start_right):
        if arr[i] < arr[min_index]:
            min_index = i
        if arr[i] > arr[max_index]:
            max_index = i

    left_index = shrinkLeft(arr,min_index,end_left)
    right_index = shrinkRight(arr,max_index,start_right)

    return (left_index,right_index)

def findEndOfLeft(arr):
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            return i-1

    return len(arr)-1

def findStartOfRight(arr):
    for i in reversed(range(0,len(arr)-1)):
        if arr[i] > arr[i+1]:
            return i+1

    return 0

def shrinkLeft(arr,min_index,start):
    comp = arr[min_index]
    for i in reversed(range(0,start)):
        if arr[i] <= comp:
            return i+1
    return 0

def shrinkRight(arr,max_index,start):
    comp = arr[max_index]
    for i in range(start,len(arr)):
        if arr[i] >= comp:
            return i-1

    return len(arr)-1
