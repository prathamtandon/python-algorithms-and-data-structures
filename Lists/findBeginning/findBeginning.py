# Given a circular linked list, return a node at the beginning of the
# loop

# Have a slow runner and a fast runner = 2x speed of slow.
# If they meet each other somewhere, then there is a loop.
# When they meet, both will be 'k' units from start of loop
# where 'k' is length of non-loop portion of the list.
# So, set slow back to head and move both slow and fast by one node
# at a time. They will meet at start of loop.

def findBeginning(head):
	fast = head
	slow = head
	
	while fast is not None and fast.get_next() is not None:
		fast = fast.get_next().get_next()
		slow = slow.get_next()
		if fast is slow:
			break
		
	if fast is None or fast.get_next() is None:
		return None
		
	slow = head
	
	while slow is not fast:
		slow = slow.get_next()
		fast = fast.get_next()
		
	return slow
