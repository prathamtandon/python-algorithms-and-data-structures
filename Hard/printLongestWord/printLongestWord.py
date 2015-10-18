# Given a list of words, find the longest word which can be
# formed by using other words from the list.


def lengthComparator(str1,str2):
    if len(str1) > len(str2):
        return -1
    elif len(str1) == len(str2):
        return 0
    else:
        return 1


def getLongestWord(dictionary):
    hashmap = {}
    for word in dictionary:
        hashmap[word] = True

    dictionary = sorted(dictionary, cmp=lengthComparator)

    for word in dictionary:
        print word
        if canBuildFromOthers(word, hashmap, True):
            return word

    return ""

def canBuildFromOthers(target, hashmap, isOriginal):
    if target in hashmap and not isOriginal:
        return hashmap[target]

    index = 1
    while index < len(target):
        left = target[0:index]
        right = target[index:]
        if left in hashmap and hashmap[left] is True and canBuildFromOthers(right, hashmap, False):
            return True
        index += 1

    hashmap[target] = False
    return False
