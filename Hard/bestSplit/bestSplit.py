# Given a document which is a string with no whitespaces, and a
# dictionary of valid words, split the document such that the
# split has minimum number of invalid words.

# This is a variation of the matrix multiplication paranthesization
# problem, where we choose a particular split if it leads to
# minimizing the total number of invalid words in the document.

# We first find where to insert the first space. The decision is made
# on the basis of the insertion which leads to minimum number of
# invalid words. Then, we insert the second space with the same idea,
# and so on. This solution will have many overlapping subproblems.
# Lets see an example:
# split(himynameispratham) =>
# h + split(imynameispratham)
# OR
# hi + split(mynameispratham)
#              ....
# split(imynameispratham) =>
# i + split(mynameispratham)
# ...
# As seen above, both split after hi and split after i result in
# same subproblem. So we can use a hashtable to cache the result
# from a specific substring or a specific start index (since we always
# end at last character of main string in all subproblems)

class ParsedResult:
    def __init__(self, invalid_count, parsed_string):
        self.invalid_count = invalid_count
        self.parsed_string = parsed_string

def bestSplit(dictionary, sentence):
    memo = [None]*len(sentence)
    r = split(dictionary, sentence, 0, memo)
    return r.parsed_string.strip() if r is not None else None

def split(dictionary, sentence, start, memo):
    if start >= len(sentence):
        return ParsedResult(0,"")
    if memo[start] is not None:
        return memo[start]

    bestInvalid = float('Inf')
    bestParsing = ""
    partial = ""
    index = start

    # Check all possible positions for the first space for current subproblem
    while index < len(sentence):
        c = sentence[index]
        # construct the word to test
        partial += c
        # check if its valid by looking up in dictionary
        invalid = 0 if partial in dictionary else len(partial)
        # check if it actually makes sense to go down this recursion path. No need if we are doing worse than current best.
        if invalid < bestInvalid:
            # get best possible spliting after current choice
            res = split(dictionary, sentence, index + 1, memo)
            # check if its better than current best
            if invalid + res.invalid_count < bestInvalid:
                bestInvalid = invalid + res.invalid_count
                bestParsing = partial + " " + res.parsed_string
                if bestInvalid == 0:
                    break
        index += 1

    memo[start] = ParsedResult(bestInvalid, bestParsing)
    return memo[start]
