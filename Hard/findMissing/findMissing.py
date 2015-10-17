# An array A contains all integers from 0 through n, except for one
# number which is missing. In this problem, we cannot access an entire
# integer in A with a single operation. The only operation we can use
# is "fetch the jth bit of A[i]" which works in O(1). Write code to
# find missing integer.

def findMissing(arr):
    return findMissingHelper(arr,0)

def findMissingHelper(arr, col):
    if col >= INEGER_SIZE:
        return 0
    oneBits = [None]*len(arr)/2
    zeroBits = [None]*len(arr)/2

    for t in arr:
        if t.fetch(col) == 0:
            zeroBits.append(t)
        else:
            oneBits.append(t)

    if len(zeroBits) <= len(oneBits):
        v = findMissingHelper(zeroBits, col+1)
        return (v << 1) | 0
    else:
        v = findMissing(oneBits, col+1)
        return (v << 1) | 1
