# Given two 32-bit numbers N and M, insert M into N starting at bit j
# ending at bit i in N. Assume, bits j through i have enough space to
# fit all of M.

# The idea is to:
# 1. Clear the bits j through i in N
# 2. Shift M so that it lines up with bits j through i
# 3. Merge M and N

def updateBits(n,m,i,j):

    # Create a mask to clear bits i through j in n. Eg: i=2,j=4. Result
    # should be 11100011.
    allOnes = ~0

    # 1s before position j, then 0s
    left = allOnes << (j+1)

    # 1s after position i
    right = ((1 << i) - 1)

    mask = left or right

    # clear bits j through i
    n_cleared = n & mask
    # move m into correct position
    m_shifted = m << i

    return n_cleared | m_shifted

