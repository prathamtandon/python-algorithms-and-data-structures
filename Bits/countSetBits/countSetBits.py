# Count the number of 1 bits in an integer.

def countSetBits(n):
    count = 0
    while n != 0:
        n &= n-1
        count += 1

    return count
