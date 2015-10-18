# Given two arrays, one shorter (with all distinct elements) and one
# longer. Find the shortest subarray in the longer array that contains
# all the elements in the shorter array. The items can appear in any
# order
# EXAMPLE
# Input
# {1,5,9}
# {7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7}
# Output [7,10]

# Suppose we have a list which tells the locations of each element
# in smallArray in bigArray.
# In above example, this is as follows:
# 1 -> {5,10,11}
# 5 -> {1,7,12}
# 9 -> {2,3,9,15}
# What is the very first valid subarray ? It starts at the min among
# the heads of each list and ends with the max among the heads. So
# in this case -> (1,5). This is our current best. How do we find the
# next best subarray ? We remove the min head from the its list and
# repeat the process.
# We can achieve better performance for extracting and maintaining
# mins using a min-heap.


