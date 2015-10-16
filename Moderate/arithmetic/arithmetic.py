# Write methods to implement multiply, subtract, and divide operations
# for integers. Use only the add operator.

# Negates the value in a. If a is positive, returns negative a
# and vice versa.
def negate(a):
    neg = 0
    newSign = 1 if a < 0 else -1
    while a != 0:
        neg += newSign
        a += newSign
    return neg

def minus(a,b):
    return a + negate(b)

def multiply(a,b):
    if a < b:
        return multiply(b,a)

    sum_val = 0
    i = abs_val(b)
    while i > 0:
        sum_val += a
        i = minus(i,1)

    if b < 0:
        sum_val = negate(sum_val)

    return sum_val

def abs_val(a):
    if a > 0:
        return a
    else:
        return negate(a)

def divide(a,b):
    if b == 0:
        raise ValueError('Cannot divide by zero')

    absa = abs_val(a)
    absb = abs_val(b)

    product = 0
    x = 0
    while product + absb <= absa:
        product += absb
        x += 1

    if (a > 0 and b > 0) or (a < 0 and b < 0):
        return x
    else:
        return negate(x)
