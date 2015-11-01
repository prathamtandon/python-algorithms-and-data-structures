# Given a string, find the longest substring which is a palindrome.

def longestPalSubstr(string):
    n = len(string)

    # memo[i][j] is True if str[i...j] is palidrome, else False.
    memo = [[False for i in range(n)] for i in range(n)]

    max_length = 1

    # All substrings of length 1 are palindromes.
    for i in range(n):
        memo[i][i] = True

    # Check for substring of length 2.
    start = 0
    for i in range(n-1):
        if string[i] == string[i+1]:
            memo[i][i+1] = True
            start = i
            max_length = 2

    # Check for lengths > 2. k is length of substring.
    for k in range(3, n+1):
        # Fix the starting index.
        for i in range(0, n-k+1):
            # Get the ending index of substring from starting index
            # i and length k.
            j = i+k-1

            # Checking for substring from ith index to jth index
            # iff string[i+1] to string[j-1] is a substring.
            if memo[i+1][j-1] is True and string[i] == string[j]:
                memo[i][j] = True

                if k > max_length:
                    start = i
                    max_length = k

    return (start,max_length)
