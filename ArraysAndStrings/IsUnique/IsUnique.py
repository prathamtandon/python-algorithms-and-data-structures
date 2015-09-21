# Accepts a string and returns true if all chars in the string are
# unique. Returns false otherwise. Assumes strings made up of
# lowercase letters 'a' through 'z'

def isUniqueChars(str):
	checker = 0
	for c in str:
		value = ord(c) - ord('a')
		if (checker & (1 << value)) > 0:
			return False
		checker |= (1 << value)
	return True
	
# Below implementation assumes ASCII strings - 128 unique chars. This
# helps to achieve both O(1) time and space complexities (actually
# O(128))

def isUniqueCharsASCII(str):
	if len(str) > 128:
		return false
	checker = [False] * 128
	for c in str:
		value = ord(c) # Returns the ASCII for a char
		if checker[value] is True:
			return False
		checker[value] = True
	return True
