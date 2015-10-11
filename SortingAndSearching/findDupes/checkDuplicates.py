# Given an array with numbers 1 through N(<=32000), and maximum
# memory of 4KB, find all duplicate entries in the array.

class BitSet:
	
	def __init__(self, size):
		self.bitvector = [0] * (size / 32 + 1)
	
	def get(self, i):
		slot_index = i / 32
		val_index = i % 32
		return self.bitvector[slot_index] & (1 << val_index) != 0
	
	def set_val(self, i):
		slot_index = i / 32
		val_index = i % 32
		self.bitvector[slot_index] |= (1 << val_index)
		
def checkDuplicates(arr, N):
	bitSet = BitSet(N)
	dupes = []
	for val in arr:
		val0 = val - 1 # bitset starts from 0, numbers start from 1
		if bitSet.get(val0):
			if val not in dupes:
				dupes.append(val)
		else:
			bitSet.set_val(val0)
	
	return dupes
			
