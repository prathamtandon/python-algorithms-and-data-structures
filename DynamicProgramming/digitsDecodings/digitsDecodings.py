# Count possible decodings of a given sequence of digits
# Let 1 represent 'A', 2 represent 'B' etc.
# Example:
# digits = "121"
# Output = 3 // "ABA", "AU", "LA"

def countDecodings (digits):
    n = len(digits)
    # memo[i] = number of decodings of digits[1...i]
    memo = [0] * (n+1)
    
    memo[0] = 1
    memo[1] = 1
    
    for i in range(2,n+1):
        if digits[i-1] > '0':
            memo[i] = memo[i-1]
        
        # if second last digit is less than 2 and last digit is <= 6,
        # then they form a valid grouping for a letter
        if digits[i-2] < '2' or (digits[i-2] == '2' and digits[i-1] < '7'): 
            memo[i] += memo[i-2]
    
    
    return memo[n]
