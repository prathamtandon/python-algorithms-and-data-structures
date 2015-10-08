# Given n stairs, and the fact that you can hop 1 step, 2 steps or 3
# steps at a time, count in how many ways you can cover the stairs.

def countWays(n):
    ways = [-1]*(n+1)
    return countWays_helper(n, ways)

def countWays_helper(n, ways):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if ways[n] > -1:
        return ways[n]

    ways[n] = countWays_helper(n-1, ways) + countWays_helper(n-2, ways) + countWays_helper(n-3, ways)
    return ways[n]
