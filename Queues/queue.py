class Queue:
	
	def __init__(self, size):
		self.head = 0
		self.tail = 0
		self.items = [None] * size
	
