from countPathsWithSum import countPathsWithSum
import pytest

class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

def test_countPathsWithSum():
	node1 = Node(10)
	node2 = Node(5)
	node3 = Node(-3)
	node4 = Node(3)
	node5 = Node(1)
	node6 = Node(11)
	node7 = Node(3)
	node8 = Node(-2)
	node9 = Node(2)
	
	node1.left = node2
	node1.right = node3
	node2.left = node4
	node2.right = node5
	node3.right = node6
	node4.left = node7
	node4.right = node8
	node5.right = node9
	
	assert(countPathsWithSum(node1, 8) == 3)
	assert(countPathsWithSum(node1, 10) == 1)
