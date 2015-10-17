# Write a function to add two numbers. You should not use + or
# any arithmetic operators.

# 1. If we add two binary numbers together, but forget to carry,
# the ith bit in the sum will be 0 only if a and b have the same
# ith bit. This is essentially XOR
# 2. If I add two numbers together but only carry, I will have a 1
# in the ith bit of the sum only if bits i-1 of a and b are both 1s.
# This is an AND, shifted.
# 3. Now recurse until there is nothing to carry.

def add(a,b):
    if b == 0:
        return a
    sum_val = a ^ b
    carry_val = (a & b) << 1
    return add(sum_val,carry_val)
