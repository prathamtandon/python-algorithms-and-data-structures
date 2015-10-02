# Given a binary tree in which each node contains an integer (positive
# or negative), return the number of paths that sum to a given value.
# The path does not need to start or end at the root or a leaf, but
# it must go downward.

# Brute-force solution
# Start at all possible nodes in the tree, for each node, travel all
# possible paths downward from that node, sum the values along the
# path and compare with given value.

def countPathsWithSum_BF(root, target_sum):
    if root is None:
        return 0

    pathsFromRoot = countPathsWithSumFromNode(root, target_sum, 0)

    pathsFromLeft = countPathsWithSum_BF(root.left, target_sum)
    pathsFromRight = countPathsWithSum_BF(root.right, target_sum)

    return pathsFromRoot + pathsFromLeft + pathsFromRight


def countPathsWithSumFromNode(node, target_sum, current_sum):
    if node is None:
        return 0
    total_paths = 0
    current_sum += node.key

    if current_sum == target_sum:
        total_paths += 1

    total_paths += countPathsWithSumFromNode(node.left, target_sum, current_sum)
    total_paths += countPathsWithSumFromNode(node.right, target_sum, current_sum)

    return total_paths

# Optimized solution
# If we see the brute force solution, suppose we see a downward path
# from a node n. Then we will see the same downward path again either
# from n.left or from n.right. So, if we could somehow compute all
# the paths during one iteration only starting at the root, that would
# be nice!
# There is a way to do this if we layout a path from root down to
# a leaf node as a linked list of nodes. For eg: let following be some
# path from root to a leaf in an arbitrary tree:
# 10 -> 5 -> 1 -> 2 -> -1 -> -1 -> 7
# Now if we maintain a running sum for each node, which is the sum
# of all nodes until that node, then we can use following logic to
# count the number of paths which sum to a target value:
# let s--y be a prefix of the actual path such that it contains x.
# s----x----y
# For each y we need to find all possible x values such that
# running_sum(y) - running_sum(x) == target_sum.
#
# How to implement this ?
# We can store the running sum at each node in a hash_table. If the
# same running sum is found again, we increment its count in the
# hash_table. Then for each node, we can lookup the value correspoing
# to (running_sum(node) - target_sum) in the hash_table. That would
# give us all the paths that sum upto the target value for a path ending
# at that node.

def countPathsWithSum(node, target_sum):
    if node is None:
        return 0
    path_count = {}
    update_hash_table(0, path_count, 1) # Needed if target path starts at root
    return countPathWithSum_helper(node, path_count, target_sum, 0)

def countPathWithSum_helper(node, path_count, target_sum, running_sum):
    if node is None:
        return 0

    total_paths = 0
    running_sum += node.key
    update_hash_table(running_sum, path_count, 1)

    desired_sum = running_sum - target_sum
    if desired_sum in path_count:
        total_paths = path_count[desired_sum]

    total_paths += countPathWithSum_helper(node.left, path_count, target_sum, running_sum)
    total_paths += countPathWithSum_helper(node.right, path_count, target_sum, running_sum)

    # This step basically removes the running sum till current node
    # as we back out to a different path in the tree.
    update_hash_table(running_sum, path_count, -1)

    return total_paths

def update_hash_table(key, table, delta):
    if key in table:
        table[key] += delta
    else:
        table[key] = 1


