# Print maximum number of As using given 4 keys.
# Key 1: Prints A on screen
# Key 2: (Ctrl A): Selects screen
# Key 3: (Ctrl C): Copy selection to buffer
# Key 4: (Ctrl V): Print buffer on screen appending it 
#                   after what has already been printed.

# Example:
# Input N = 3
# Output = 3
# A, A, A

# Input N = 7
# Output = 9
# A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V

# Input N = 11
# Output = 27
# A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V, Ctrl A, Ctrl C, Ctrl V,
# Ctrl V

# a) For N < 7, the output is N itself. 
# b) Ctrl V can be used multiple times to print current buffer 
# The idea is to compute the optimal string length for N keystrokes
# by using a simple insight. The sequence of N keystrokes which 
# produces an optimal string length will end with a suffix of Ctrl-A
# a Ctrl C, followed by only Ctrl Vs.
# If we loop from N-3 to 1 and choose each of these values for the 
# break point, we will have the maximum of optimal lengths for various
# break points, and this will give us the optimal length for N keystrokes.

def findMaxAs (N):
    
    if N <= 6:
        return N
    
    # screen[i] = max number of A's that can be printed with i keystrokes.
    screen = [0] * N
    
    # For N <= 6, screen[N] = N
    for i in range(1,7):
        screen[i - 1] = i
    
    # For N > 6, we select each of the points from N-3 to 1
    # as the points for printing a sequence of Ctrl A, Ctrl C and then
    # all Ctrl Vs. Using this technique, we find the optimal length 
    # for each of the Ns from N = 7 onwards. Finally we return
    # screen[N-1]
    for i in range(7,N+1):
        screen[i-1] = 0
        
        for break_point in reversed(range(1,i-3)):
            # if break point is at break_point, we will have
            # 
            cur = (i-break_point-1) * screen[break_point-1]
            if cur > screen[i-1]:
                screen[i-1] = cur
    
    return screen[N-1]
