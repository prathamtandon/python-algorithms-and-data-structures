# Implementation of interval trees.
# Operations supported:
# 1. Insert a new interval (low, high)
# 2. Delete an interval (low, high)
# 3. Search an interval i: Returns the interval which overlaps with i.

# General idea: In interval tree T, for a node n, for all nodes m in left
# subtree of n, m.low <= n.low, for all nodes m in right subtree of n,
# m.low >= n.low. Also, each node stores the maximum value for high
# attribute for entire subtree rooted at that node.

class Interval:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __eq__(self, other):
        return self.low == other.low and self.high == other.high

class IntervalTreeNode:
    def __init__(self, interval=None, left=None, right=None):
        self.interval = interval
        self.left = left
        self.right = right
        self.max_high = interval.high

    def insert(self, interval):
        if self.max_high < interval.high:
            self.max_high = interval.high
        if self.interval.low >= interval.low:
            if self.left is None:
                self.left = IntervalTreeNode(interval)
            else:
                self.left.insert(interval)
        else:
            if self.right is None:
                self.right = IntervalTreeNode(interval)
            else:
                self.right.insert(interval)

    def is_overlap(self, interval):
        return not self.interval.high <= interval.low and not self.interval.low >= interval.high

    def search(self, interval):
        cur = self
        while cur is not None and not cur.is_overlap(interval):
            if cur.left is not None and cur.left.max_high >= interval.low:
                cur = cur.left
            else:
                cur = cur.right

        return cur

