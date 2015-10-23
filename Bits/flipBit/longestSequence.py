# Given an integer, you can flip exactly one bit from a 0 to a 1. Write
# code to find the length of the longest sequence of 1st you could
# create.
# EXAMPLE
# Input 1775 (or 11011101111)
# Output 8

# The main idea is to consider each number to be a sequence of 0s and 1s.
# So, when we replace a 0 by 1, we are basically merging the two
# adjacent 1 sequences to create a new "mega sequence".
# Then, we just need to go through the list once and make following
# choices:
# 1. If count of zeros = 1, we just take left and right length and plus 1
# 2. If count of zeros > 1, we take either side and plus 1.

SEQUENCE_LENGTH = 32

def rshift(val, n):
    return (val % 0x100000000) >> n

def longestSequence(n):
    if n == -1:
        return SEQUENCE_LENGTH
    sequences = get_alternating_sequences(n)
    return find_longest_sequence(sequences)

# Returns list of the sequence sizes. The sequence starts off with the
# number of 0s (which might be 0) and then alternates with the counts of
# each value.
def get_alternating_sequences(n):
    sequences = []

    searching_for = 0
    counter = 0

    for i in range(SEQUENCE_LENGTH):
        if (n & 1) != searching_for:
            sequences.append(counter)
            searching_for = 1 if searching_for is 0 else 0
            counter = 0
        counter += 1
        n = rshift(n,1) # We want to shift the sign bit too.

    sequences.append(counter)

    return sequences

def find_longest_sequence(seq):
    max_seq = 1

    i = 0
    while i < len(seq):
        zeros_seq = seq[i]
        ones_seq_right = seq[i-1] if i-1 >= 0 else 0
        ones_seq_left = seq[i+1] if i+1 < len(seq) else 0

        this_seq = 0
        if zeros_seq == 1: # Can merge
            this_seq = ones_seq_left + ones_seq_right + 1
        elif zeros_seq > 1:
            this_seq = 1 + max(ones_seq_right, ones_seq_left)
        else:
            this_seq = max(ones_seq_right, ones_seq_left)

        max_seq = max(max_seq, this_seq)
        i += 2

    return max_seq
