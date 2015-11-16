# Given a number n, find the sum of all digits from 1 through n.
# Example:
# Input: n = 5
# Output: Sum of digits from 1 through 5 = 15
# Input: n = 12
# Output: Sum of digits from 1 through 12 = 51

# The basic idea is as follows:
# sum(9) = 1 + 2 + 3 + ... + 9 = 9 * (9 + 1) / 2 = 45
# sum(99) = 45 + (10 + 45) + (20 + 45) + ... + (90 + 45) = sum(9)*10 + 45*10
# sum(999) = sum(99)*10 + 45*100 

# In general we can compute sum(10^d - 1) as
# sum(10^d - 1) = sum(10^d-1 - 1)*10 + 45*10^d-1

# Algorithm:
# Sum(n):
# 1. Find the number of digits minus 1 in n. Let this value be 'd'.
#    For 328, d is 2.
# 2. Compute some of digits in numbers from 1 to 10^d - 1. Let this 
#    value be w. For 328, w is sum of digits from 1 to 99.
# 3. Find most significant digit (msd) is n. For 328, msd is 3.
# 4. Overall sum is sum of following terms:
#    a) Find the sum of digits in 1 to "msd*(10^d - 1)". For 328,
#       this is the sum of digits from 1 to 299.
#       Sum(299) = Sum(99) + (1*100 + Sum(99)) + (2*100 + Sum(99))
#    or Sum(299) = 3*Sum(99) + (1 + 2)*100
#    b) Find the sum of digits from msd*10^d to n.
#       For 328, this is sum of digits from 300 to 328.
#       This is computed as 3*29 + recursive call "Sum(28)"
from math import log10, ceil

def sumOfDigitsFrom1ToN(n):
    # base case
    if n < 10:
        return n*(n+1)/2
    
    # d is number of digits minus 1 in n.
    d = int(log10(n))
    
    # Compute sum of digits from 1 through 10^d-1
    # memo[0] = 0
    # memo[1] = 45 (sum of digits from 1 through 9)
    # memo[2] = memo[1]*10 + 45*10^1 = 900 (sum of digits from 1 through 99)
    # memo[3] = memo[2]*100 + 45*10^2 = 13500 (sum of digits from 1 through 999) 
    memo = [0]*(d+1)
    memo[0] = 0
    memo[1] = 45
    for i in range(2,d+1):
        memo[i] = memo[i-1]*10 + 45*int(ceil(pow(10,i-1)))
    
    # computing 10^d    
    p = int(ceil(pow(10,d)))
    
    msd = n/p
    
    return (msd*memo[d] + (msd*(msd-1)/2)*p) + (msd*(1+n%p) + sumOfDigitsFrom1ToN(n%p))
