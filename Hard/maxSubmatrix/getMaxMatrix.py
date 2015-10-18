# Given an NxN matrix of positive and negative integers, write code
# to find the submatrix with largest possible sum.

class Submatrix:
    def __init__(self,r1,c1,r2,c2,sm):
        self.row1 = r1
        self.col1 = c1
        self.row2 = r2
        self.col2 = c2
        self.sm = sm

    def getSum(self):
        return self.sm

def getMaxMatrix(matrix):
    best = None
    rowCount = len(matrix)
    colCount = len(matrix[0])
    sumThrough = precomputeSums(matrix)

    for row1 in range(rowCount):
        for row2 in range(row1,rowCount):
            for col1 in range(colCount):
                for col2 in range(col1,colCount):
                    sum_val = computeSum(sumThrough,row1,col1,row2,col2)
                    if best is None or best.getSum() < sum_val:
                        best = Submatrix(row1,col1,row2,col2,sum_val)


    return best

def precomputeSums(matrix):
    sumThrough = [[0]*len(matrix[0]) for i in range(len(matrix))]

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            left = matrix[r][c-1] if c > 0 else 0
            top = matrix[r-1][c] if r > 0 else 0
            overlap = matrix[r-1][c-1] if c > 0 and r > 0 else 0
            sumThrough[r][c] = left + top - overlap + matrix[r][c]

    return sumThrough

def computeSum(sumThrough,r1,c1,r2,c2):
    topAndLeft = sumThrough[r1-1][c1-1] if r1 > 0 and c1 > 0 else 0
    left = sumThrough[r2][c1-1] if c1 > 0 else 0
    top = sumThrough[r1-1][c2] if r1 > 0 else 0
    full = sumThrough[r2][c2]

    return full-left-top+topAndLeft
