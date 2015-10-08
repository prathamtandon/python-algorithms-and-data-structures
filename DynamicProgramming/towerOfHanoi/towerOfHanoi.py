# Tower of Hanoi

class Tower:
    def __init__(self, i):
        self.disks = []
        self.index = i

    def add(self, d):
        if len(self.disks) > 0 and self.disks[len(self.disks)-1] <= d:
            raise ValueError('Error placing disk: ' + str(d))
        else:
            self.disks.append(d)

    def moveTop(self,t):
        top = self.disks.pop()
        t.add(top)

    def moveDisks(self, n, destination, buf):
        if n > 0:
            self.moveDisks(n-1, buf, destination)
            self.moveTop(destination)
            buf.moveDisks(n-1,destination,self)

