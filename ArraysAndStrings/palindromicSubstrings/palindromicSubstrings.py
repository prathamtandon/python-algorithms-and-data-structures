# Given a string of ASCII characters, find all palindromic substrings.

def palindromeSubStr(string):
    hashmap = {}
    n = len(string)

    # table for storing results (2 rows for even and odd-length palindromes)
    memo = [[0 for i in range(n+1)],[0 for i in range(n+1)]]

    # Find all substring palindromes from the given input string.
    # Insert 'guards' to iterate easily over string
    string = '@' + string + '#'

    for j in range(0,2):
        # length of palindrome radius
        radius = 0
        memo[j][0] = 0

        i = 1
        while i <= n:
            # Attempt to expand palindrome centered at 'i'
            while string[i-radius-1] == string[i+j+radius]:
                # Increase radius of current substring
                radius += 1

            # Assigning the found palindromic length to odd/even length array
            memo[j][i] = radius
            k = 1
            while (memo[j][i-k] != radius-k) and k < radius:
                memo[j][i+k] = min(memo[j][i-k], radius-k)
                k += 1

            radius = max(radius-k,0)
            i += k

    # remove guards
    string = string[1:n]

    # Put all obtained palindromes in a hashmap to find distinct palindromes.
    hashmap[string[0]] = 1
    for i in range(1, n+1):
        for j in range(0,2):
            for r in reversed(range(1,memo[j][i])):
                hashmap[string[i-r-1,2*r+j] = 1

        hashmap[string[i]] = 1

    return hashmap.keys()
