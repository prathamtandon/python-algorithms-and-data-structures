class Node(object):
	
	def __init__(self, key=None, prev_node=None, next_node=None):
		self.key = key
		self.prev_node = prev_node
		self.next_node = next_node
		
	def get_key(self):
		return self.key
	
	def get_next(self):
		return self.next_node;
	
	def set_next(self, new_next):
		self.next_node = new_next
	
	def get_prev(self):
		return self.prev_node
	
	def set_prev(self, new_prev):
		self.prev_node = new_prev
