import Queue
import bisect

class Trie:
	
	def __init__(self):
		self.key = None
		self.value = None
		self.children = []
	
	def insert_key(self, key, value):
		cur = self
		for i, c in enumerate(key):
			match = None
			for child in cur.children:
				if child.key == key[:i + 1]:
					match = child
					break
			if match is None:
				new_child = Trie()
				new_child.key = key[:i + 1]
				keys = [child.key for child in cur.children]
				insert_at = bisect.bisect_left(keys, new_child.key)
				cur.children.insert(insert_at, new_child)
				cur = new_child
			else:
				cur = match
		cur.value = value
	
	def has_key(self, key):
		cur = self
		for i, c in enumerate(key):
			match = None
			for child in cur.children:
				if child.key == key[:i + 1]:
					match = child
					break
			if match is None:
				return False
			else:
				cur = match
		return True
		
	def retrieve_val(self, key):
		cur = self
		for i, c in enumerate(key):
			match = None
			for child in cur.children:
				if child.key == key[:i + 1]:
					match = child
					break
			if match is None:
				return None
			else:
				cur = match
		return cur.value
		
	def starts_with_prefix(self, key):
		items = []
		if not self.has_key(key):
			return items
		cur = self
		for i, c in enumerate(key):
			for child in cur.children:
				if child.key == key[:i + 1]:
					cur = child
					break
		
		Q = Queue.Queue()
		Q.put(cur)
		while not Q.empty():
			cur = Q.get()
			if cur.value is not None:
				items.append(cur.key)
			for child in cur.children:
				Q.put(child)
		
		return items
	
	def lexicographic_sort(self):
		def lexicographic_sort_helper(cur, acc):
			if cur.key is None and len(cur.children) == 0:
				return acc
			if cur.value is not None:
				acc.append(cur.key)
			for child in cur.children:
				lexicographic_sort_helper(child, acc)
			return acc
		
		return lexicographic_sort_helper(self, [])
			
