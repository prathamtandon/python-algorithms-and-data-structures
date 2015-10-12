# A BST which supports getRank(x) which returns the number of
# elements less than or equal to x.

# The idea is to store the size of left subtree at each node.
# While looking for the rank, if the element lies to right of
# a node, we return the rank as rank(element) + left_size + 1

class RankNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.left_size = 0

    def insert(self, key):
        if self.key > key:
            if self.left is None:
                self.left = RankNode(key)
            else:
                self.left.insert(key)
            self.left_size += 1
        else:
            if self.right is None:
                self.right = RankNode(key)
            else:
                self.right.insert(key)

    def getRank(self, key):
        if self.key == key:
            return self.left_size
        elif self.key > key:
            if self.left is None:
                return -1
            else:
                return self.left.getRank(key)
        else:
            if self.right is None:
                return -1
            else:
                right_side = self.right.getRank(key)
                return self.left_size + right_side + 1

class Rank:
    def __init__(self):
        self.root = None

    def track(self, x):
        if self.root is None:
            self.root = RankNode(x)
        else:
            self.root.insert(x)

    def getRank(self, x):
        if self.root is None:
            return -1
        else:
            return self.root.getRank(x)
