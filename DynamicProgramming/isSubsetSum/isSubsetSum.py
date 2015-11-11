# Given a set of non negative integers, and a value sum, determine if
# there is a subset of the given set with sum equal to given sum.

# Example: set = [3, 34, 4, 12, 5, 2] ,sum = 9
# Output:  True ,There is a subset (4, 5) with sum 9.

# isSubsetSum(set,n,sum) = isSubsetSum(set,n-1,sum-set[n-1]) || isSubsetSum(set,n-1,sum)

# Base case: 
# isSubsetSum(set, n, sum) is False if n == 0 and sum > 0
# isSubsetSum(set, n ,sum) is True if sum == 0

# Also ignore set[n-1] is set[n-1] > sum

# Let memo[i][j] be True if set[0...j-1] has a subset with sum i and False otherwise.
# Finally we return memo[sum][n]

def isSubsetSum(set_elems, n, sum_val):
        memo = [[False for i in range(n+1)] for i in range(sum_val+1)]
        
        # True if sum == 0
        for i in range(n+1):
                memo[0][i] = True
        
        # False if n == 0
        for i in range(1,sum_val+1):
                memo[i][0] = False

        # Fill memo in bottom up manner
        for i in range(1,sum_val+1):
                for j in range(1,n+1):
                        memo[i][j] = memo[i][j-1]
                        if i >= set_elems[j-1]:
                                memo[i][j] = memo[i][j] or memo[i-set_elems[j-1]][j-1]
                                
        
        return memo[sum_val][n]
