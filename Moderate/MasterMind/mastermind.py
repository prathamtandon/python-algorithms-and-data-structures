# Game of Master Mind.

class Result:
    def __init__(self):
        self.hits = 0
        self.pseudo_hits = 0

    def __str__(self):
        return "(" + self.hits + "," + self.pseudo_hits + ")"

def code(c):
    if c is 'B':
        return 0
    elif c is 'G':
        return 1
    elif c is 'R':
        return 2
    elif c is 'Y':
        return 3
    else:
        return -1

MAX_COLORS = 4

def estimate(guess, solution):
    if len(guess) != len(solution):
        return None

    res = Result()
    frequencies = [0]*MAX_COLORS

    for i in range(len(guess)):
        if guess[i] == solution[i]:
            res.hits += 1
        else:
            idx = code(solution[i])
            frequencies[idx] += 1

    for i in range(len(guess)):
        idx = code(guess[i])
        if idx >= 0 and frequencies[idx] > 0 and guess[i] != solution[i]:
            res.pseudo_hits += 1
            frequencies[idx] -= 1

    return res
