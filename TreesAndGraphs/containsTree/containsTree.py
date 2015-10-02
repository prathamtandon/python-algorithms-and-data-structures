# T1 and T2 are very large binary trees, with T1 much bigger than
# T2. Create an algorithm to determine if T2 is a subtree of T1.

def containsTree(t1, t2):
    if t2 is None:
        return True

    return subTree(t1, t2)

def subTree(t1, t2):
    if t1 is None:
        return False

    if t1.key == t2.key:
        return matchTree(t1, t2)
    else:
        return subTree(t1.left, t2) or subTree(t1.right, t2)

def matchTree(t1, t2):
    if t1 is None and t2 is None:
        return True
    elif t1 is None or t2 is None:
        return False
    return t1.key == t2.key and matchTree(t1.left, t2.left) and matchTree(t1.right, t2.right)
