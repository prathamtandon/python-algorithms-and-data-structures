# Given a number n, find count of all binary sequences of length 2n
# such that sum of first n bits is same as sum of last n bits.

# Examples:
# Input n = 1, Output 2, 00 and 11
# Input n = 2, Output 6, 0000,0101,1010,1111,0110,1001
# and so on.

# The main idea is as follows:
# Compare first and last bits. 
# 1. If they are equal, sum of remaining bits should be equal
# 2. If first bit is 1 and last bit is 0, sum of n-1 bits on right
#    should be 1 more than n-1 bits on left.
# 3. If first bit is 0 and last bit is 1, sum of n-1 bits on left
#    should be 1 more than n-1 bits on right.

# diff is expected difference between first half digits and last
# half digits.

def equalSum_helper(n, diff, memo):
        # We cannot cover diff of more than n with 2n bits. (n=4 11110000, max-diff=4)
        if abs(diff) > n:
                return 0
        
        # n = 1, 00 and 11
        if n == 1 and diff == 0:
                return 2
        
        # n = 1, 10
        if n == 1 and abs(diff) == 1:
                return 1
                
        if memo[n][n+diff] != -1:
                return memo[n][n+diff]
        
        # Three cases: 
        # 1st bit is 0 and last bit is 1, diff between first half and second half should be increased by 1
        # 1st bit is 1 and last bit is 0, diff between first half and second half should be decreased by 1
        # 1st bit and second bit is same, n-1 bits on both sides have same value
        res = equalSum_helper(n-1,diff+1,memo) + equalSum_helper(n-1,diff-1,memo) + 2*equalSum_helper(n-1,diff,memo)
        
        memo[n][n+diff] = res
        
        return res

def equalSum(n):
        memo = [[-1 for i in range(2*n)] for i in range(2*n)]
        return equalSum_helper(n, 0, memo)
