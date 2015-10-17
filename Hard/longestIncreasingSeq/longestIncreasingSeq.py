# Given a sequence of numbers, find the longest increasing
# subsequence.

def longestIncreasingSeq(arr):
    # solutions[i] stores the longest increasing sequence ending at arr[i]
    solutions = {}
    # the overall longest increasing sequence
    bestSeq = []

    for i in range(len(arr)):
        # get the longest increasing sequence ending in arr[i]
        longestAtIndex = bestSeqAtIndex(arr,solutions,i)
        # add to solutions[i]
        solutions[i] = longestAtIndex
        # compare with current best seq
        bestSeq = betterSeq(bestSeq, longestAtIndex)

    return bestSeq

def bestSeqAtIndex(arr,solutions,index):
    bestAtIndex = []
    # for all i < index, check if arr[index] can be appended at end to get a longer sequence.
    for i in range(index):
        solution = solutions[i]
        if canAppend(solution, arr[index]):
            bestAtIndex = betterSeq(bestAtIndex, solution)

    res = list(bestAtIndex)
    res.append(arr[index])
    return res

def betterSeq(seq1, seq2):
    if len(seq1) > len(seq2):
        return seq1
    else:
        return seq2

def canAppend(seq, value):
    if seq is None or len(seq) == 0:
        return True
    else:
        return seq[len(seq)-1] <= value


