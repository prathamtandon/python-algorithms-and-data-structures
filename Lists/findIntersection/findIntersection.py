# Given two singly linked lists, return the intersecting node or null
# if they don't intersect. Intersection is based on reference and not
# value.

# Returns the length and last node of a linked list.
def get_tail_and_length(head):
    cur = head
    length = 0
    while cur.get_next() is not None:
        cur = cur.get_next()
        length += 1

    return { 'tail': cur, 'length': length }

# Returns the kth node from start of a linked list.
def get_kth_node(head, k):
    cur = head
    while k > 0:
        cur = cur.get_next()
        k -= 1

    return cur

def findIntersection(head1, head2):
    if head1 is None or head2 is None:
        return None

    result1 = get_tail_and_length(head1)
    result2 = get_tail_and_length(head2)

    if result1['tail'] is not result2['tail']:
        return None

    longer = head1 if result1['length'] > result2['length'] else head2
    shorter = head1 if longer is head2 else head2

    longer = get_kth_node(longer, abs(result1['length'] - result2['length']))

    while shorter is not longer:
        shorter = shorter.get_next()
        longer = longer.get_next()

    return shorter


# An alternate approach (not implemented) here is by having an 
# additional "visited" field on each node in the two lists.
# Travel one list and set the visited field on each node touched.
# Then, while travelling the second list, the first node with 
# visited = True should be the intersecting node.
