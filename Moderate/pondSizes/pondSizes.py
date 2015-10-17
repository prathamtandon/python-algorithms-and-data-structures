# Given an integer matrix representing a plot of land. Value in a
# cell is the height above sea level. A value of zero indicates water.
# A pond is a region of water connected horizontally, vertically or
# diagonally. Size of pond is total number of connected water cells.
# Compute sizes of all ponds in the matrix.

def computePondSizes(land):
    pondSizes = []
    for r in range(len(land)):
        for c in range(len(land[0])):
            if land[r][c] == 0:
                size = computeSize(land,r,c)
                pondSizes.append(size)

    return pondSizes


def computeSize(land,r,c):
    if r < 0 or c < 0 or r >= len(land) or c >= len(land[0]) or land[r][c] != 0:
        return 0

    size = 1
    land[r][c] = -1
    size += computeSize(land,r+1,c)
    size += computeSize(land,r-1,c)
    size += computeSize(land,r,c+1)
    size += computeSize(land,r,c-1)
    size += computeSize(land,r+1,c+1)
    size += computeSize(land,r+1,c-1)
    size += computeSize(land,r-1,c+1)
    size += computeSize(land,r-1,c-1)

    return size

