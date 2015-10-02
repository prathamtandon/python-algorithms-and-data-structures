# Find first common ancestor of two nodes in a binary tree.

def commonAncestor(root, p, q):
	# Error check - one node is not in the tree
	if not covers(root, p) or not covers(root, q):
		return None
	return ancestor_helper(root, p, q)


def ancestor_helper(root, p, q):
	if root is None:
		return None
	elif root is p:
		return p
	elif root is q:
		return q
	
	is_p_on_left = covers(root.left, p)
	is_q_on_left = covers(root.left, q)
	
	if is_p_on_left != is_q_on_left:
		# p and q in different subtrees -> root should be FCA
		return root
	
	child_side = root.left if is_p_on_left else root.right
	
	return ancestor_helper(child_side, p, q)

def covers(root, node):
	if root is None:
		return False
	if root is node:
		return True
	return covers(root.left, node) or covers(root.right, node)


# Alternate method (Optimized):
# covers searches the left and right subtrees of root and then returns
# one of them. It then takes the returned node and searches its 
# left and right subtrees again. So each subtree is searched over and
# over again.

def commonAncestor_optimized(root, p, q):
	if root is None:
		return None
	
	if root is p and root is q:
		return root
	
	x = commonAncestor(root.left, p, q)
	if x is not None and x is not p and x is not q:
		return x
	
	y = commonAncestor(root.right, p, q)
	if y is not None and y is not p and y is not q:
		return y
	
	if x is not None and y is not None:
		return root
	elif root is p or root is q:
		return root
	else:
		return x if x is not None else y
