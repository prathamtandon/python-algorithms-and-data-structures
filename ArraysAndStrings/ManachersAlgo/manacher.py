# Longest palindromic substring using Manacher Algorithm.

def findLongestPalindrome(string):
    if string is None or len(string) == 0:
        return ''

    # string2 will have 2*N+1 elements: N elements from string, N-1 boundaries between elements and 2 boundaries at either ends.
    string2 = add_boundaries(string)
    # spans is the array of palindromic spans for each element in string2, from center to either outermost element.
    # E.g: A palindrome with 3 elements has palindromic span of 1.
    spans = [0]*len(string2)
    # center is the center of current palindromic sequence. E.g: length of palindrome = spans[center]*2 + 1
    center = 0
    # right is the position of rightmost end of current palindromic sequence. E.g: right = center + spans[center]
    right = 0
    # index is the position of an element in string2 whose palindromic span is being determined.
    # index2 is the mirrored position of index around center.
    # E.g.: for center = 5, {index,index2} = {6,4},{7,3},{8,2} etc. index2 = 2*center - index

    # The walking indices to compare if two elements are the same
    m = 0
    n = 0
    for index in range(1,len(string2)):
        if index > right:
            spans[index] = 0
            m = index - 1
            n = index + 1
        else:
            index2 = 2*center - index
            if spans[index2] < (right-index):
                spans[index] = spans[index2]
                m = -1 # The signals bypassing the while loop below
            else:
                spans[index] = right-index
                n = right + 1
                m = index*2 - n

        while m >= 0 and n < len(string2) and string2[m] == string2[n]:
            spans[index] += 1
            m -= 1
            n += 1
        if (index + spans[index]) > right:
            center = index
            right = index + spans[index]

        max_span = 0
        max_center = -1
        for i in range(1,len(string2)):
            if max_span < spans[i]:
                max_span = spans[i]
                max_center = i

        result = string2[max_center-max_span:max_center+max_span+1]
        return remove_boundaries(result)

def add_boundaries(string):
    if string is None or len(string) == 0:
        return ['|','|']

    result = ['0']*(2*len(string) + 1)
    i = 0
    while i < len(result)-1:
        result[i] = '|'
        result[i+1] = string[i/2]
        i += 2

    result[len(result)-1] = '|'
    return result

def remove_boundaries(string):
    if string is None or len(string) == 0:
        return ''

    result = ['0']*((len(string)-1)/2)

    for i in range(len(result)):
        result[i] = string[2*i+1]

    return ''.join(result)
