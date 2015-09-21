# Replaces all spaces in a string with '%20'. Assumes that string
# has sufficient space at the end to hold the additional characters,
# and that you are given the 'true' length of string
# EXAMPLE:
# Input    "Mr John Smith    ",13
# Output   "Mr%20John%20Smith"

def URLify(str, length):
	char_array = list(str)
	
	space_count = 0
	for i in xrange(length):
		if char_array[i] == ' ':
			space_count += 1
	
	new_length = length + space_count * 2
	
	for i in reversed(xrange(length)):
		if char_array[i] == ' ':
			char_array[new_length - 1] = '0'
			char_array[new_length - 2] = '2'
			char_array[new_length - 3] = '%'
			new_length -= 3
		else:
			char_array[new_length - 1] = char_array[i]
			new_length -= 1
	
	return ''.join(char_array)
