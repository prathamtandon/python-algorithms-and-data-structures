# Given a real number between 0 and 1(eg. 0.72) that is passed in
# as a float, print the binary representation. If number cannot be
# presented accurately in binary, print "ERROR"

def printBinary(num):
    if num >= 1 or num <= 0:
        return

    binary = []
    binary.append('.')

    while num > 0:
        if len(binary) >= 32:
            raise ValueError('ERROR')

        r = num * 2

        if r >= 1:
            binary.append('1')
            num = r - 1
        else:
            binary.append('0')
            num = r


    return ''.join(binary)

