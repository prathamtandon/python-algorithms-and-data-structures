# Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree.
# EXAMPLE
#                2
#               / \
#              1   3
# OUTPUT: {2,1,3},{2,3,1}

# At any node n, a smaller subproblem would be to get
# all sequences from n.left and all sequences from n.right
# and prepend n at the start of all "weavings" of those sequences.
# We define "weaving" of two sequences as follows:
# weave([1,2],[3,4]) = [1,2,3,4],[1,3,2,4],[3,1,4,2],[3,4,1,2]
# ie all possible orderings of items from the two lists while still
# maintaining the relative order between elements.

def allSequences(node):
    result = []

    if node is None:
        return result

    prefix = [].append(node.key)

    leftSequences = allSequences(node.left)
    rightSequences = allSequences(node.right)

    for l_seq in leftSequences:
        for r_seq in rightSequences:
            weaved = []
            weaveLists(l_seq, r_seq, weaved, prefix)
            results = results + weaved

    return results


def weaveLists(first, second, results, prefix):
    if len(first) == 0 or len(second) == 0:
        result = list(prefix)
        result = result + first
        result = result + second
        results.append(result)
        return

    head_first = first.pop(0)
    prefix.append(head_first)
    weaveLists(first, second, results, prefix)
    prefix.pop()
    first.insert(0, head_first)

    head_second = second.pop(0)
    prefix.append(head_second)
    weaveLists(first, second, results, prefix)
    prefix.pop()
    second.insert(0, head_second)
