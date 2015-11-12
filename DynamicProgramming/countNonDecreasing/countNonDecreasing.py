# A number is non-decreasing if every digit (except the first one)
# is greater than or equal to previous digit. For example,
# 223, 4455567, 899, are non-decreasing numbers

# Given the number of digits n, find the count of non-decreasing
# numbers with n digits.

# One way to think of the problem is, 
# count of n digit numbers = (count of n-1 digit numbers ending with 9) 
# + (count of n-1 digit numbers ending with 8) 
# ...
# + (count of n-1 digit numbers ending with 0)

def countNonDecreasing(n):
        
        # memo[i][j] = # of numbers ending in digit i and length = j
        memo = [[0 for i in range(n+1)] for i in range(10)]
        
        for i in range(10):
                memo[i][1] = 1
                
        
        for digit in range(10):
                for length in range(2,n+1):
                        # sum of all numbers of length-1 which have
                        # their last digit x <= digit
                        for x in range(digit+1):
                                memo[digit][length] += memo[x][length-1]
                                
        
        count = 0
        
        # Total non-decreasing numbers of length n will be
        # memo[0][n] + memo[1][n] + memo[2][n] + ... + memo[9][n]
        for i in range(10):
                count += memo[i][n]
        
        return count
