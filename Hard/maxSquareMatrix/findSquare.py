# Given a square matrix, where each cell is either black or white.
# Design an algorithm to find the maximum subsquare such that all
# four borders are filled with black pixels.

# The main idea is to check all subsquares of progressively smaller
# sizes (as we need to find the biggest subsquare) and return as
# soon as we find one with all black edges. A small optimization
# or pre-processing would be to create a matrix c such that c[i][j]
# holds the # of cells which are black below c[i][j] and # of
# cells which are black to the right of c[i][j]

class Subsquare:
    def __init__(self,row,col,size):
        self.row = row
        self.col = col
        self.size = size

class SquareCell:
    def __init__(self):
        self.zerosRight = 0
        self.zerosBelow = 0

    def __str__(self):
        return '(' + str(self.zerosRight) + ',' + str(self.zerosBelow) + ')'

def findSquare(matrix):
    processed = processMatrix(matrix)

    for i in reversed(range(1,len(matrix)+1)):
        square = findSquareWithSize(processed,i)
        if square is not None:
            return square

    return None

def findSquareWithSize(matrix,squareSize):
    # On an edge of length N, there are N-sz+1 squares of size sz.
    count = len(matrix) - squareSize + 1

    for r in range(count):
        for c in range(count):
            if isSquare(matrix,r,c,squareSize):
                return Subsquare(r,c,squareSize)

    return None

def isSquare(matrix,r,c,size):
    topLeft = matrix[r][c]
    topRight = matrix[r][c+size-1]
    bottomLeft = matrix[r+size-1][c]

    # check top, left, bottom and right edges respectively.
    if topLeft.zerosBelow < size or topLeft.zerosRight < size or topRight.zerosBelow < size or bottomLeft.zerosRight < size:
        return False

    return True

def processMatrix(matrix):
    processed = [[None]*len(matrix) for i in range(len(matrix))]

    for r in reversed(range(len(matrix))):
        for c in reversed(range(len(matrix))):
            rightZeros = 0
            belowZeros = 0

            # only need to process if cell is black
            if matrix[r][c] == 0:
                rightZeros += 1
                belowZeros += 1

                # bound checks
                if c+1 < len(matrix):
                    rightCell = processed[r][c+1]
                    rightZeros += rightCell.zerosRight
                if r+1 < len(matrix):
                    belowCell = processed[r+1][c]
                    belowZeros += belowCell.zerosBelow

            sc = SquareCell()
            sc.zerosRight = rightZeros
            sc.zerosBelow = belowZeros
            processed[r][c] = sc

    return processed

