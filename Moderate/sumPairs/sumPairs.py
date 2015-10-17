# Given an array and a target, return all pairs of values
# which have sum equal to target. Assuming distinct values in array.

def sumPairs(arr, target):
    if arr is None or len(arr) == 0:
        return
    hashmap = {}
    pairs = []


    for val in arr:
        if target-val in hashmap and hashmap[target-val] > 0:
            pairs.append((val,target-val))
            hashmap[target-val] -= 1
        if val in hashmap:
            hashmap[val] += 1
        else:
            hashmap[val] = 1


    '''
    Use code below to handle input with non-distinct values

    for val in arr:
        if val in hashmap:
            hashmap[val] += 1
        else:
            hashmap[val] = 1

    for val in arr:
        if target-val in hashmap and hashmap[target-val] > 0 and hashmap[val] > 0:
            pairs.append((val,target-val))
            hashmap[target-val] -= 1
    '''


    return pairs

# Solution 2: Using sorting.

def sumPairs2(arr,target):
    arr = sorted(arr)
    first = 0
    last = len(arr)-1

    pairs = []

    while first < last:
        s = arr[first] + arr[last]
        if s == target:
            pairs.append(arr[first],arr[last])
            first += 1
            last -= 1
        elif s < target:
            first += 1
        else:
            last -= 1

    return pairs

