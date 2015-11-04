# Transform S into T.
# For eg: S = "abba", T = "^#a#b#b#a#$"
# ^ and $ are sentinels appended to each end to avoid bounds checking.

def pre_process(s):
    n = len(s)
    if n == 0:
        return '^$'
    result = '^'

    for i in range(n):
        result += '#' + s[i]

    result += '#$'
    return result

def longest_palindrome(s):
    T = pre_process(s)
    n = len(T)
    p = [0]*n
    c = 0
    r = 0

    for i in range(1,n-1):
        i_mirror = 2*c-i

        if r>i:
            p[i] = min(r-i,p[i_mirror])

        # Attempt to expand palindrome centered at i
        while T[i+1+p[i]] == T[i-1-p[i]]:
            p[i] += 1

        # If palindrome centered at i expand past r,
        # adjust center based on expanded palindrome.
        if i+p[i] > r:
            c = i
            r = i + p[i]

    max_len = 0
    center_index = 0
    for i in range(1,n-1):
        if p[i] > max_len:
            max_len = p[i]
            center_index = i

    return s[(center_index-1-max_len)/2:(center_index-1+max_len)/2]

