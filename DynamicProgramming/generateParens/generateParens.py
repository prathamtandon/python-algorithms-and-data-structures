# Print all valid combinations of n pairs of parantheses

def generateParens(n):
	result = []
	addParen(result, n, n, [])
	return result

def addParen(result, leftRem, rightRem, chars):
	if leftRem < 0 or rightRem < leftRem: # invalid state
		return 
	if leftRem == 0 and rightRem == 0:
		result.append("".join(chars))
	else:
		if leftRem > 0: # we could add a left paren as long as there are remaining left parens
			cloned = list(chars)
			cloned.append("(")
			addParen(result, leftRem-1, rightRem, cloned)
		if rightRem > leftRem: # we could addd a right paren as long as there are less right parens than there are left
			cloned = list(chars)
			cloned.append(")")
			addParen(result, leftRem, rightRem-1, cloned)
