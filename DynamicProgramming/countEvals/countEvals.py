# Given an input string representing a boolean expr, and a result,
# count the number of ways of paranthesizing the expr to obtain
# the desired result.

# The basic idea is very similar to matrix multiplication paranthesization
# to minimize the number of scalar multiplications. We find all possible
# last operations and find the number of paranthesizations for everything
# to left and everything to right of that point.

def to_boolean(one_string):
    return True if one_string == '1' else False

def countEvals(boolean_expr, result, hashmap):
    if boolean_expr == "":
        return 0
    if len(boolean_expr) == 1:
        return to_boolean(boolean_expr) == result
    if boolean_expr in hashmap:
        if result is True and hashmap[boolean_expr][0] != -1:
            return hashmap[boolean_expr][0]
        elif result is False and hashmap[boolean_expr][1] != -1:
            return hashmap[boolean_expr][1]
    else:
        hashmap[boolean_expr] = [-1,-1]

    ways = 0
    i = 1
    while i < len(boolean_expr):
        c = boolean_expr[i]
        left_expr = boolean_expr[0:i]
        right_expr = boolean_expr[i+1:]
        left_true = countEvals(left_expr, True, hashmap)
        left_false = countEvals(left_expr, False, hashmap)
        right_true = countEvals(right_expr, True, hashmap)
        right_false = countEvals(right_expr, False, hashmap)

        total_ways = (left_true + left_false)*(right_true + right_false)
        total_true = 0

        if c is '^':
            total_true = left_true*right_false + left_false*right_true
        elif c is '|':
            total_true = left_true*right_true + left_false*right_true + left_true*right_false
        elif c is '&':
            total_true = left_true*right_true

        ways += total_true if result is True else total_ways - total_true
        i += 2

    index = 0 if result is True else 1
    hashmap[boolean_expr][index] = ways
    return ways



