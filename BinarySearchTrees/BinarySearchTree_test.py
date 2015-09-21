from Node import Node
from BinarySearchTree import BinarySearchTree
import pytest

def test_insert():
	bs_tree = BinarySearchTree()
	keys = [6, 5, 7, 2, 5, 8]
	for key in keys:
		node = Node()
		node.key = key
		bs_tree.insert(node)
	assert(bs_tree.search(6).key == 6)
	assert(bs_tree.search(5).key == 5)
	assert(bs_tree.search(7).key == 7)
	assert(bs_tree.search(8).key == 8)

def test_search():
	bs_tree = BinarySearchTree()
	assert(bs_tree.search(2) is None)
	keys = [6, 5, 7, 2]
	for key in keys:
		node = Node()
		node.key = key
		bs_tree.insert(node)
	assert(bs_tree.search(6).key == 6)
	assert(bs_tree.search(7).key == 7)
	assert(bs_tree.search(8) is None)

def test_minimum():
	bs_tree = BinarySearchTree()
	assert(bs_tree.minimum(bs_tree.root) is None)
	keys = [6, 5, 7, 2, 5, 8]
	for key in keys:
		node = Node()
		node.key = key
		bs_tree.insert(node)
	assert(bs_tree.minimum(bs_tree.root).key == 2)
	subtree = bs_tree.search(7)
	assert(bs_tree.minimum(subtree).key == 7)

def test_maximum():
	bs_tree = BinarySearchTree()
	assert(bs_tree.minimum(bs_tree.root) is None)
	keys = [6, 5, 7, 2, 5, 8]
	for key in keys:
		node = Node()
		node.key = key
		bs_tree.insert(node)
	assert(bs_tree.maximum(bs_tree.root).key == 8)
	subtree = bs_tree.search(5)
	assert(bs_tree.maximum(subtree).key == 5)
	
def test_successor():
	bs_tree = BinarySearchTree()
	keys = [6, 5, 7, 2, 5, 8]
	for key in keys:
		node = Node()
		node.key = key
		bs_tree.insert(node)
	assert(bs_tree.successor(bs_tree.root).key == 7)
	subtree = bs_tree.search(2)
	assert(bs_tree.successor(subtree).key == 5)
	subtree = bs_tree.search(8)
	assert(bs_tree.successor(subtree) is None)
	
def test_predecessor():
	bs_tree = BinarySearchTree()
	keys = [6, 5, 7, 2, 5, 8]
	for key in keys:
		node = Node()
		node.key = key
		bs_tree.insert(node)
	assert(bs_tree.predecessor(bs_tree.root).key == 5)
	subtree = bs_tree.search(7)
	assert(bs_tree.predecessor(subtree).key == 6)
	subtree = bs_tree.search(2)
	assert(bs_tree.predecessor(subtree) is None)

def test_delete():
	bs_tree = BinarySearchTree()
	keys = [5, 2, -4, 3, 12, 9 ,21, 19, 25]
	for key in keys:
		node = Node()
		node.key = key
		bs_tree.insert(node)
	# delete leaf
	bs_tree.delete(bs_tree.search(-4))
	assert(bs_tree.search(-4) is None)
	assert(bs_tree.search(2).left is None)
	
	
	# delete node with one child
	bs_tree.delete(bs_tree.search(2))
	assert(bs_tree.search(2) is None)
	assert(bs_tree.root.left.key == 3)
	
	
	# delete node with two children
	bs_tree.delete(bs_tree.search(12))
	assert(bs_tree.root.right.key == 19)
	assert(bs_tree.search(19).left.key == 9)
	assert(bs_tree.search(19).right.key == 21)

	
	# delete root
	bs_tree.delete(bs_tree.root)
	assert(bs_tree.root.key == 9)
	assert(bs_tree.root.left.key == 3)
	assert(bs_tree.root.right.key == 19)
