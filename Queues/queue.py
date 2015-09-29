class Queue:

    def __init__(self, size):
        self.head = 0
        self.tail = 0
        self.items = [None] * size

    def enqueue(self, x):
        if self.head == self.tail + 1:
            raise Exception("Overflow")
        self.items[self.tail] = x
        if self.tail == len(self.items):
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        if self.head == self.tail:
            raise Exception("Underflow")
        x = self.items[self.head]
        if self.head == len(self.items):
            self.head = 0
        else:
            self.head += 1
        return x

    def contains(self, x):
        return x in self.items
