from Node import Node

class LinkedList(object):
	
	def __init__(self, head=None):
		self.head = head
	
	def search(self, key):
		cur = self.head
		while cur is not None and cur.get_key() is not key:
			cur = cur.get_next()
		return cur
	
	def insert(self, key):
		node = Node(key)
		node.set_next(self.head)
		if self.head is not None:
			self.head.set_prev(node)
		self.head = node

	def delete(self, key):
		node = self.search(key)
		if node is None:
			raise ValueError("Key not in list")
		if node.get_prev() is not None:
			node.get_prev().set_next(node.get_next())
		else:
			self.head = node.get_next()
		if node.get_next() is not None:
			node.get_next().set_prev(node.get_prev())

	def size(self):
		cur = self.head
		count = 0
		while cur is not None:
			count += 1
			cur = cur.get_next()
		return count
