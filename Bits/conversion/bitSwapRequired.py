# Determine the number of bits you would need to flip to convert
# integer A to integer B.

# The idea is to do bitwise XOR to decide which bits are different
# between A and B.

def bitSwapRequired(a,b):
    count = 0
    c = a ^ b
    while c != 0:
        count += c & 1
        c >>= 1

    return count
