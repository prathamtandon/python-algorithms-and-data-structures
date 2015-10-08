# Permutations of a string with duplicates

def getPermsDupes(string):
	if string is None:
		return None
	frequencies = get_frequency_table(string)
	result = []
	getPermsDupes_helper("",len(string),frequencies,result)
	return result

def get_frequency_table(string):
	table = {}
	for c in string:
		if c in table:
			table[c] += 1
		else:
			table[c] = 1
	return table

def getPermsDupes_helper(prefix,remaining,frequencies,result):
	if remaining == 0:
		result.append(prefix)
		return
	for c in frequencies:
		count = frequencies[c]
		if count > 0:
			frequencies[c] = count-1
			getPermsDupes_helper(prefix + c,remaining-1,frequencies,result)
			frequencies[c] = count
