# Numbers are randomly generated and passed to a method. Write a program
# to find and maintain the median value as new values are generated.

# We use two heaps - a max heap to track all elements smaller than
# median and a min heap to track all elements greater than median.
# When size(max-heap) == size(min-heap), then median value will be
# max-heap.top() + min-heap.top() / 2. If size(max-heap) > size(min-heap)
# then median will be max-heap.top()

# Note : We are using a hack to implement max-heap as python's heapq
# just implements a min-heap

import heapq

maxheap = []
minheap = []

def addNewNumber(randomNumber):
    if len(maxheap) == len(minheap):
        if len(minheap) > 0 and randomNumber > minheap[0]:
            heapq.heappush(maxheap, -heapq.heappop(minheap))
            heapq.heappush(minheap, randomNumber)
        else:
            heapq.heappush(maxheap, -randomNumber)
    else:
        if randomNumber < maxheap[0]:
            heapq.heappush(minheap, abs(heapq.heappop(maxheap)))
            heapq.heappush(maxheap, -randomNumber)
        else:
            heapq.heappush(minheap, randomNumber)

def getMedian():
    if len(maxheap) == 0:
        return 0
    elif len(maxheap) == len(minheap):
        return (float(abs(maxheap[0])) + minheap[0])/2
    else:
        return maxheap[0]
