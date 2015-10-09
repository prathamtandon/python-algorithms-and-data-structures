# Eight Queen Problem

GRID_SIZE = 8

def placeQueens(row, columns, results):
    if row == GRID_SIZE:
        results.append(list(columns))
    else:
        for col in range(GRID_SIZE):
            if checkValid(row, col, columns):
                # By convention, if columns[r] = c, it means in rth row,
                # queen is placed at cth column.
                columns[row] = col
                placeQueens(row+1, columns, results)

def checkValid(row1, col1, columns):
    for row2 in range(row1):
        col2 = columns[row2]

        if col1 == col2:
            return False

        rowDiff = row1 - row2
        colDiff = abs(col1 - col2)

        if rowDiff == colDiff:
            return False

    return True
