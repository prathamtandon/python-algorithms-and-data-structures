# Finds the kth to last element in a linked list

def kthToLast(lst, k):
    count = 0
    first = lst.head
    while count < k:
        if first is None:
            return None
        first = first.get_next()
        count += 1
    second = lst.head
    while first is not None:
        first = first.get_next()
        second = second.get_next()
    return second
