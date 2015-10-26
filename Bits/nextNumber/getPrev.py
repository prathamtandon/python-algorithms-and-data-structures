def getPrev(n):
    temp = n
    c0 = 0
    c1 = 0
    while temp & 1 == 1:
        c1 += 1
        temp >>= temp

    if temp == 0:
        return -1

    while ((temp & 1) == 0) and (temp != 0)):
        c0 += 1
        temp >>= 1

    p = c0 + c1
    n &= ((~0) << (p + 1))

    mask = (1 << (c1 + 1)) - 1
    n |= mask << (c0 - 1)

    return n
