class BinarySearchTree:
	
	def __init__(self):
		self = None
		
	def inorder_walk(self):
		if self is not None:
			inorder_tree_walk(self.left)
			print(self.key, end=" ")
			inorder_tree_walk(self.right)
	
	def search(self, key):
		cur = self
		while cur is not None and cur.key is not key:
			if cur.key < key:
				cur = cur.left
			else:
				cur = cur.right
		return cur
	
	def minimum(self):
		cur = self
		while cur is not None and cur.left is not None:
			cur = cur.left
		return cur
	
	def maximum(self):
		cur = self
		while cur is not None and cur.right is not None:
			cur = cur.right
		return cur
	
	def successor(self, node):
		if node is not None and node.right is not None:
			return self.minimum(node.right)
		parent = node.parent
		while parent is not None and parent.right == node:
			node = parent
			parent = node.parent
		return parent
	
	def predecessor(self, node):
		if node is not None and node.left is not None:
			return self.maximum(node.left)
		parent = node.parent
		while parent is not None and parent.left == node:
			node = parent
			parent = node.parent
		return parent
		
	def insert(self, node):
		parent = None
		cur = self
		while cur is not None:
			parent = cur
			if node.key < cur.key:
				cur = cur.left
			else:
				cur = cur.right
		node.parent = parent
		if parent is None: # tree was empty
			self = node
		elif node.key < parent.key:
			parent.left = node
		else:
			parent.right = node
			
	# replaces src node with target node in the BST 
	def transplant(self, src, target):
		if src.parent is None:
			self = target
		elif src == src.parent.left:
			src.parent.left = target
		else:
			src.parent.right = target
		if target is not None:
			target.parent = src.parent
			
	def delete(self, node):
		if node.left is None:
			self.transplant(node, node.right)
		elif node.right is None:
			self.transplant(node, node.left)
		else:
			# promote successor to take place of node
			successor = self.minimum(node.right)
			if successor.parent is not node:
				# promote successor's right in place of successor
				self.transplant(successor, successor.right)
				successor.right = node.right
				successor.right.parent = successor
			self.transplant(node, successor)
			successor.left = node.left
			successor.left.parent = successor
		
			
		
