# Count the number of trailing zeroes in n!

# The main idea is that zeroes are introduced by multipying 2 and
# 5 or multiples of 2 and multiples of 5. Since, there would
# be more multiples of 2 than 5, we can just count the multiples of
# 5. Two count multiples of 5 -
# Say the number is n. Then there are n/5 multiples of 5, n/25
# multiples of 25, n/125 of 125 and so on.

def countZeroes(n):
    if n < 0:
        return 0
    i = 5
    count = 0
    while n/i > 0:
        count += n/5
        i *= 5

    return count
