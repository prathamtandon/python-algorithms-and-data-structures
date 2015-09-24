# Partitions a linked list around a value x such that all values
# less than x come before all values greater than or equal to x.

def partition_list(lst, x):
    head = lst.head
    tail = lst.head

    cur = lst.head
    while cur is not None:
        nxt = cur.get_next()
        if cur.get_key() < x:
            cur.set_next(head)
            head.set_prev(cur)
            head = cur
        else:
            tail.set_next(cur)
            cur.set_prev(tail)
            tail = cur
        cur = nxt

    tail.set_next(None)

    return head
