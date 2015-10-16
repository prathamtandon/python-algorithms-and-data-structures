# Give a pattern and a value, determine if value matches pattern.
# For eg: pattern = aabab
#         value = catcatgocatgo
# Return true

def doesMatch(pattern, value):
    if len(pattern) == 0:
        return len(value) == 0

    main = pattern[0]
    alt = 'a' if main is 'b' else 'b'
    countMain = countOf(pattern,main)
    countAlt = len(pattern) - countMain
    firstAlt = pattern.index(alt)

    size = len(value)
    mainMaxSize = size / countMain

    for mainSize in range(mainMaxSize):
        first = value[0:mainSize]
        remaining_length = size - countMain * mainSize
        if countAlt == 0 or remaining_length % countAlt == 0:
            altIndex = firstAlt * mainSize
            altSize = 0 if countAlt is 0 else remaining_length/countAlt
            second = "" if countAlt is 0 else value[altIndex:altIndex+altSize]
            cand = buildFromPattern(pattern,first,second)
            if value == cand:
                return True

    return False


def buildFromPattern(pattern,first,second):
    main = pattern[0]
    parts = []
    for c in pattern:
        if c == main:
            parts.append(first)
        else:
            parts.append(second)

    return "".join(parts)

def countOf(pattern,c):
    count = 0
    for char in pattern:
        if c == char:
            count += 1

    return count


