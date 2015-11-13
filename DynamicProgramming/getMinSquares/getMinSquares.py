# Given a number n, find the minimum number of squares that sum to n.
# Eg:
# Input n = 100
# Output = 1
# as 100 = 10^2
# Also, 100 = 5^2 + 5^2 + 5^2 + 5^2
# But this representation requires 4 squares.

# The basic recurrence is as follows:
# If n <= 3, then return n
# Else
#       minSquares(n) = min { 1 + minSquares(n-x*x) } where x >= 1 and
#                       x*x <= n

def getMinSquares(n):
        
        # memo[i] denotes the minimum number of squares that sum to i
        memo = [0] * (n+1)
        
        memo[0] = 0
        memo[1] = 1 # 1^2
        memo[2] = 2 # 1^2 + 1^2
        memo[3] = 3 # 1^2 + 1^2 + 1^2
        
        for i in range(4,n+1):
                # max value is i as i can always be represented as 1^2 + 1^2 +... i times
                memo[i] = i
                
                for x in range(1,i):
                        temp = x * x
                        if n < temp:
                                break
                        else:
                                memo[i] = min(memo[i], 1 + memo[i - temp])
        
        
        return memo[n]


