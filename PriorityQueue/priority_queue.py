from math import floor;

class PriorityQueue:

    def __init__(self):
        self.items = []

    def parent(self, i):
        return int(floor(i/2))

    def left(self, i):
        return 2*i+1

    def right(self, i):
        return 2*i+2

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        largest = i

        if l < len(self.items) and self.items[l] > self.items[largest]:
            largest = l
        if r < len(self.items) and self.items[r] > self.items[largest]:
            largest = r

        if largest != i:
            temp = self.items[i]
            self.items[i] = self.items[largest]
            self.items[largest] = self.items[i]
            self.max_heapify(largest)

    def get_max(self):
        return self.items[0]

    def extract_max(self):
        max_priority = self.items[0]
        self.items[0] = self.items[len(self.items)-1]
        self.items.pop()
        self.max_heapify(0)
        return max_priority

    def update_key(self, key, index):
        self.items[index] = key
        i = index
        while i >= 0 and self.items[self.parent(i)] < self.items[i]:
            temp = self.items[self.parent(i)]
            self.items[self.parent(i)] = self.items[i]
            self.items[i] = temp
            i = self.parent(i)

    def insert_key(self, key):
        self.items.append(-1)
        self.update_key(key, len(self.items)-1)

    def contains(self, key):
        return key in self.items

