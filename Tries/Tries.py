class Trie:
	
	def __init__(self):
		self.key = None
		self.value = None
		self.children = []
	
	def insert_key(self, key, value):
		cur = self
		for i in enumerate(key):
			match = None
			for child in cur.children:
				if child.key == key[:i]:
					match = child
					break
			if match == None:
				new_child = new Trie()
				new_child.key = key[:i]
				cur.children.append(new_child)
				cur = new_child
			else:
				cur = match
		cur.value = value
	
	def has_key(self, key):
		cur = self
		for i in enumerate(key):
			match = None
			for child in cur.children:
				if child.key == key[:i]:
					match = child
					break
			if match == None:
				return False
			else:
				cur = match
		return True
		
	def retrieve_val(self, key):
		cur = self
		for i in enumerate(key):
			match = None
			for child in cur.children:
				if child.key == key[:i]:
					match = child
					break
				if match == None:
					return None
				else:
					cur = match
		return cur.value
		
	def starts_with_prefix(self, key):
		items = []
		if not self.has_key(key):
			return items
		cur = self
		for i in enumerate(key):
			for child in cur.children:
				if child.key == key[:i]:
					cur = child
					break
		
		Q = new Queue()
		Q.put(cur)
		while not Q.empty():
			cur = Q.get()
			if cur.value is not None:
				items.append(cur.key)
			for child in cur.children:
				Q.put(child)
		
		return items
			
