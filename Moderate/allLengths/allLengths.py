# Given a bunch of planks of different lengths - shorter and longer,
# generate all possible lengths of a diving board made by placing
# exactly k planks from end to end.

def allLengths(k, total, shorter, longer, lengths, visited):
    if k == 0:
        lengths.add(total)
        return

    if str(k) + str(total) in visited:
        return

    allLengths(k-1, total + shorter, shorter, longer, lengths, visited)
    allLengths(k-1, total + longer, shorter, longer, lengths, visited)
    visited[str(k) + str(total)] = True

def getAllLengths(k, shorter, longer):
    lengths = set([])
    visited = {}
    allLengths(k, 0, shorter, longer, lengths, visited)
    return lengths
