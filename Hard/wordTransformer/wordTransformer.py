# Given two words of equal length that are in a dictionary, write a
# method to transform one word into another word by changing only
# one letter at a time. The new word you get in each step must be in
# a dictionary.
# EXAMPLE
# Input DAMP,LIKE
# DAMP->LAMP->LIMP->LIME->LIKE

# The main idea is to first get all valid words from the dictionary
# which are one edit away from the startWord and then do a DFS from
# these words until a path is found to stopWord.
# To find the words that are one edit away, we use a wild card
# approach. For eg: consider a sample dictionary like {'ill','all','ale'}
# Then the different wildcards would be: i_l,il_,_ll,al_ etc.
# Now, if a wildcard can be reached from multiple words, then all
# those words are one edit away from each other.

def transform(start, stop, words):
    wildCardToWordList = createWildCardToWordMap(words)
    visited = set([])
    return transformHelper(visited, start, stop, wildCardToWordList)

def createWildCardToWordMap(words):
    wildCardToWords = {}
    for word in words:
        linked = getWildCardRoots(word)
        for linkedWord in linked:
            if linkedWord in wildCardToWords:
                wildCardToWords[linkedWord].append(word)
            else:
                wildCardToWords[linkedWord] = [word]

    return wildCardToWords

def getWildCardRoots(word):
    linked = []
    for i in range(len(word)):
        w = word[0:i] + '_' + word[i+1:]
        linked.append(w)

    return linked

def transformHelper(visited, startWord, stopWord, wildCardToWordMap):
    if startWord == stopWord:
        path = [startWord]
        return path
    elif startWord in visited:
        return None

    visited.add(startWord)
    words = getValidLinkedWords(startWord, wildCardToWordMap)

    for word in words:
        path = transformHelper(visited, word, stopWord, wildCardToWordMap)
        if path is not None:
            path.insert(0, startWord)
            return path

    return None

def getValidLinkedWords(word, wildCardToWordMap):
    result = []
    linked = getWildCardRoots(word)

    for linkedWord in linked:
        words = wildCardToWordMap[linkedWord]
        for w in words:
            if w != word:
                result.append(w)

    return result

