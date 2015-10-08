# Write a method to compute all permutations of a string with unique chars

def getPerms(string):
	if len(string) == 0:
		return [""]
	permutations = []
	first = string[0]
	remainder = string[1:]
	words = getPerms(remainder)
	for word in words:
		for j in range(0, len(word)+1):
			permutations.append(insertCharAt(word, first, j))
	
	return permutations

def insertCharAt(word, char, index):
	start = word[0:index]
	end = word[index:]
	return start + char + end


def getPerms2(remainder):
	results = []
	length = len(remainder)
	if length == 0:
		results.append("")
		return results
	
	for i in range(0, length):
		before = remainder[0:i]
		after = remainder[i+1:]
		partials = getPerms2(before + after)
		for partial in partials:
			results.append(remainder[i] + partial)
	
	return results
