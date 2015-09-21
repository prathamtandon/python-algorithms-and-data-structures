# Accepts two strings and returns true if one is a permutaiton of the
# other. Assumes ASCII strings

def sort(str):
	return ''.join(sorted(str))

def IsPermutationWithSort(source, target):
	if len(source) != len(target):
		return False
	return sort(source) == sort(target)

def IsPermutationWithLetterCount(source, target):
	if len(source) != len(target):
		return False
	letters = [0] * 128
	for c in source:
		letters[ord(c)] += 1
	for c in target:
		letters[ord(c)] -= 1
		if letters[ord(c)] < 0:
			return False
	return True
	
