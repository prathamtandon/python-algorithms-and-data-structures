# Given a positive number, print the next smallest and the next
# largest number that have the same number of 1 bits in their
# binary representation.

def getNext(n):
    c = n
    # let p denote the position of first non-trailing 0 ie a zero which is followed by 1s
    c0 = 0 # number of zeros to right of position p
    c1 = 0 # number of ones to right of position p

    # while there are training zeros and c > 0
    while (c & 1) == 0 and (c != 0):
        c0 += 1
        c >>= 1

    while (c & 1) == 1:
        c1 += 1
        c >>= 1

    # If n = 111...1100...000, then there is no bigger number with same number of 1s
    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1

    p = c0 + c1

    n |= (1 << p) # Flip rightmost non trailing zero
    n &= ~((1 << p) - 1) # Clear all bits to right of 1
    n |= (1 << (c1 - 1)) - 1 # Insert (c1-1) ones on the right
    return n
