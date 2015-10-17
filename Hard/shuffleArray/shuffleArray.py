# Write a method to shuffle a deck of cards. It must be a perfect
# shuffle - in other words, each of the 52! permutations of hte deck
# has to be equally likely. Assume that you are given a random number
# generator that is perfect.

# Suppose we know how to shuffle n-1 cards. Then to shuffle n cards,
# we pick a random position from a shuffle of n-1 cards and swap it
# with the nth card.
from random import random

def rand(lower, higher):
    return lower + int(random() * (higher - lower + 1))

def shuffleArrayRecursive(cards, i):
    if i == 0:
        return cards

    shuffleArrayRecursive(cards, i-1) # Shuffle earlier part
    k = rand(0,i)

    temp = cards[i]
    cards[i] = cards[k]
    cards[k] = temp

    return cards

def shuffleArrayIterative(cards):
    for i in range(len(cards)):
        k = rand(0, i)
        temp = cards[i]
        cards[i] = cards[k]
        cards[k] = temp
