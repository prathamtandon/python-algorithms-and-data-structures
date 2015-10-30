# Given a room with N people, and a function knows(A,B) which
# returns true if A knows B and false otherwise, find a celebrity
# if present (A person who does not know anyone but everyone else knows
# the person).

def haveAcquintance(relationships, a, b):
    return relationships[a-1][b-1]

def celebrity(relationships, size):
    people = []
    for i in range(1, size + 1):
        people.append(i)

    a = people.pop()
    b = people.pop()

    print a
    print b

    while len(people) != 1:
        if haveAcquintance(relationships, a, b) == 1:
            # if a knows b, then a cannot be celebrity.
            a = people.pop()
        else:
            # if a does not know b, then b cannot be celebrity.
            b = people.pop()

    c = people.pop()

    # compare last candidate
    if haveAcquintance(relationships, c, b) == 1:
        c = b
    if haveAcquintance(relationships, c, a) == 1:
        c = a

    for i in range(1, size + 1):
        if i != c:
            # c must not know i
            if haveAcquintance(relationships, c, i) == 1:
                return -1

            # i must know i
            if haveAcquintance(relationships, i, c) != 1:
                return -1        

    return c
