# Given an M x N matrix in which each row and column is sorted, write
# a method to find an element

def findElement(matrix, x):
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col > -1:
        if matrix[row][col] == x:
            return True
        elif matrix[row][col] < x:
            row += 1
        else:
            col -= 1

    return False
