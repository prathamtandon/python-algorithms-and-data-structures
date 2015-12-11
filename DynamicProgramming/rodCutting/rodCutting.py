# Given a rope of length n meters, cut the rope in different parts
# of integral lengths in a way that maximizes product of lengths of
# all parts. You must make atleast one cut. Assume that length of rope
# is more than 2 meters.

# Example:
# ropeCutting (2) = 1*1 = 1
# ropeCutting (3) = (1*2) or (2*1) = 2
# If a cut is made at position k, then there are 2 ropes - one of
# length k and another of length n-k.
# What we need to decide is whether after making a cut at position k,
# do we need to further cut the part of length n-k?
# so, ropeCut(n) = max(i*(n-i), i*ropeCut(n-i)) for all positions 
# i = 1,2,3,...,n

def ropeCutting (n):
    memo = [0] * (n+1)
    memo[0] = 0
    memo[1] = 0
    
    for i in range(1,n+1):
        cur_max = -float('inf')
        for j in range(1, (i/2+1)):
            cur_max = max(cur_max, j*(i-j), j*memo[i-j])
        memo[i] = cur_max
    
    return memo[n]
    
    
