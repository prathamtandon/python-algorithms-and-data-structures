# Linear time pattern searching algorithm.

# For a string str[0...n-1], Z[i] stores length of longest substring
# starting from str[i] which is also a prefix of str[0...n-1].
# Example:
# Index            0   1   2   3   4   5   6   7   8   9  10  11
# Text             a   a   b   c   a   a   b   x   a   a   a   z
# Z values         X   1   0   0   3   1   0   0   2   2   1   0

# More Examples:
# str  = "aaaaaa"
# Z[]  = {x, 5, 4, 3, 2, 1}

# str = "aabaacd"
# Z[] = {x, 1, 0, 2, 1, 0, 0}

# str = "abababab"
# Z[] = {x, 0, 6, 0, 4, 0, 2, 0}

# The idea is to construct a new string P$T, where P is pattern, $ is a
# special separator character, T is the text. Build the Z array for
# concatenated string. In Z array, if Z value is equal to pattern length
# at any index, then pattern is present at that index.

# We can construct Z array in linear time.

def get_z_array(string, Z):
    n = len(string)

    Left = 0
    Right = 0
    k = 0

    # Let [Left,Right] be a window that matches with a prefix of string.
    for i in range(1,n):

        # If i > Right, nothing matches so will calculate Z[i] using
        # naive way.
        if i > Right:
            Left = i
            Right = i

            # Right-Left is 0 at start. So, it will start checking from
            # 0th index. For example, for 'ababab' and i = 1, the value
            # of Right remains 0 and Z[i] becomes 0. For 'aaaaaa' and i =1
            # Z[i] and Right become 5.
            while Right < n and string[Right-Left] == string[Right]:
                Right += 1
            Z[i] = Right-Left
            Right -= 1
        else:
            # k = i-Left so k corresponds to number which matches [Left,Right]
            # interval.
            k = i-Left

            # if Z[k] is less than remaining interval
            # then Z[i] will be equal to Z[k].
            # For example, str = "ababab", i = 3, Right = 5
            # and Left = 2
            if (Z[k] < Right-i+1):
                Z[i] = Z[k]
            elif (Z[k] > Right-i+1):
                Z[i] = Right-i+1
            else:
                # else start from Right and check manually.
                Left = i
                while Right < n and string[Right-Left] == string[Right]:
                    Right += 1
                Z[i] = Right-Left
                Right -= 1

def search(text, pattern):
    concat = pattern + '$' + text
    l = len(concat)
    Z = [0] * l
    get_z_array(concat, Z)

    for i in range(l):
        if Z[i] == len(pattern):
            return i-len(pattern)-1

    return -1
