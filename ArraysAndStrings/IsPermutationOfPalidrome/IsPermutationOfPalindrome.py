# Accepts a string and returns if it is a permutation of a 
# palindrome. 
# Example
# Input "Tact Coa"
# Output True ("taco cat","atco cta" etc.)

# There are several ways of doing this. The important thing is 
# to understand that we just have to tell if the string is a
# permutation of a pallindrome, we need not find the palindrome itself.
# This means that if the given string satisfies the properties of a
# pallindrome - ie it should have even number of same type of letters
# with at most one letter which occurs just once (eg. "abba" or "aba")
# we can tell whether the string is a permutation of some palindrome.

# To actually find the counts of different letters, there are several
# ways of doing this. An elegant solution involves having
# an integer bitmask with one index for each letter in the input string.
# Each time we encounter a letter, we "toggle" the corresponding bit
# in the mask. After scanning the entire string, if the bitmask value
# is zero or if it has exactly one bit set, we return true 

def IsPermutationOfPalindrome(phrase):
	bit_vector = create_bit_vector(phrase)
	return bit_vector == 0 or is_exactly_one_bit_set(bit_vector)

# maps a char to an integer, like 'a' is mapped to 0, 'b' to 1,
# 'c' to 2 and so on	
def get_char_number(c):
	if ord('a') <= ord(c) <= ord('z'):
		return ord(c) - ord('a')
	elif ord('A') <= ord(c) <= ord('Z'):
		return ord(c) - ord('A')
	return -1

def create_bit_vector(phrase):
	vector = 0
	for c in phrase:
		value = get_char_number(c)
		vector = toggle(vector, value)
	return vector

# toggles the bit in vector at given index. 
def toggle(vector, index):
	if index < 0:
		return vector
	mask = 1 << index
	if (vector & mask) == 0:
		vector |= mask
	else:
		vector &= ~mask
	return vector

# we can check if a bitmask has just one bit as '1' by subtracting
# the mask by 1 and the ANDing the result with the mask. AND result
# is zero if there is exactly one bit set in the mask
def is_exactly_one_bit_set(vector):
	return ((vector - 1) & vector) == 0
	
