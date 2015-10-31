# Find four elements a,b,c and d in an array such that a+b=c+d.

def findPairs(arr):
    hashmap = {}

    result = []
    size = len(arr)
    for i in range(0,size):
        for j in range(i+1,size):

            res = arr[i] + arr[j]
            if res not in hashmap:
                hashmap[res] = (arr[i],arr[j])
            else:
                return ((hashmap[res],(arr[i],arr[j])))

    return None
