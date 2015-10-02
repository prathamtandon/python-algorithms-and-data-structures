from commonAncestor import commonAncestor
import pytest

class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

def test_commonAncestor():
	node1 = Node(20)
	node2 = Node(10)
	node3 = Node(30)
	node4 = Node(5)
	node5 = Node(15)
	node6 = Node(3)
	node7 = Node(7)
	node8 = Node(17)
	node9 = Node(24)
	
	node1.left = node2
	node1.right = node3
	node2.left = node4
	node2.right = node5
	node4.left = node6
	node4.right = node7
	node5.right = node8
	
	'''
				20
			   / \
			  10  30
			 / \
			 5  15
			/\    \
		    3 7    17
	'''
	
	assert(commonAncestor(node1, node7, node8) is node2)
	assert(commonAncestor(node1, node2, node3) is node1)
	assert(commonAncestor(node1, node2, node9) is None)
	

