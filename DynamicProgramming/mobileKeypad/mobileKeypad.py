# Given a mobile keypad, and a value N, output the number
# of valid numbers that can be formed of length N.
# Valid moves include only the top, bottom, left and right neighbors
# of a digit on the keypad. '*' and '#' cannot be pressed.

keypad = [['1','2','3'],['4','5','6'],['7','8','9'],['*','0','#']]

def is_special_key (i,j):
    return keypad[i][j] in ['#','*']

def is_valid_keypress (i,j):
    return i >= 0 and i < len(keypad) and j >= 0 and j < len(keypad[0]) and not is_special_key(i,j)

def mobileKeypad (n):
    if n <= 0:
        return 0
    if n == 1:
        return 10
    
    # let memo[i][j] be # of numbers of length j starting with
    # digit i.
    memo = [[0 for i in range(n+1)] for i in range(10)]

    for i in range(10):
        memo[i][0] = 0
        memo[i][1] = 1
    
    # loop all smaller lengths 2,3,...,n-1,n
    for k in range(2,n+1):
        # for each length, loop all keys of keypad
        for i in range(len(keypad)):
            for j in range(len(keypad[0])):
                if not is_special_key(i,j):
                    digit = int(keypad[i][j])
                    memo[digit][k] = memo[digit][k-1]
                    
                    # check all four neighbours of digit
                    neighbours = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
                    for neighbour in neighbours:
                        row_index = neighbour[0]
                        col_index = neighbour[1]
                        if is_valid_keypress (row_index, col_index):
                            neighbour_digit = int(keypad[row_index][col_index])
                            memo[digit][k] += memo[neighbour_digit][k-1]
    
    total_count = 0
    for i in range(10):
        total_count += memo[i][n]
    
    return total_count
                        
