# Multiplying two numbers without using the * operator. You could
# use addition, subtraction and bit shifting but try to minimize the
# use of those operations.

def minProduct(a,b):
    smaller = a if a < b else b
    bigger = a if smaller == b else b
    return minProduct_helper(smaller, bigger)

def minProduct_helper(smaller, bigger):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    half = smaller >> 1
    halfProduct = minProduct_helper(half, bigger)
    if smaller % 2 == 0:
        return halfProduct << 1
    else:
        return (halfProduct << 1) + bigger
