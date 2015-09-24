# Removes duplicates from an unsorted linked list without using
# temporary buffer

def deleteDupes(lst):
    cur = lst.head
    while cur is not None:
        runner = cur.get_next()
        while runner is not None:
            if runner.get_key() == cur.get_key():
                runner.get_prev().set_next(runner.get_next())
                if runner.get_next() is not None:
                    runner.get_next().set_prev(runner.get_prev())
            runner = runner.get_next()
        cur = cur.get_next()

