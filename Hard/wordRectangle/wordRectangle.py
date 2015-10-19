# Given a list of words, create a largest possible rectangle of letters
# such that every row forms a word(from left to right) and every
# column forms a word(from top to bottom). All rows must be same length
# and all columns must be same height.

# We start by grouping all words of same length together. Lets call this
# grouping D such that D[i] contains a list of words of length i.

# Next, since we are looking for largest rectangle, its size can be
# at the max - len(longest_word) * len(longest_word).
# So we start iterating from biggest possible rectangle to smallest
# and attempt to build a rectangle of words of length l and height h.
# We could build such a rectangle by taking all ordered sets of words
# of length l and then check to see if the columns are also valid words.
# But this would lead to lot of extra work. What if, while building 
# the rectangle, we could quickly find out if there is a word
# starting with a given column prefix before having to build till height
# h ? This could save us a lot of extra work. We can do this using a
# Trie made from prefix strings. We can have a Trie of all possible
# words grouped on size, so we can quickly check to see if a particular
# prefix will return a valid word of say height h.

# So we start by trying out all possible length l words. Say we have
# k words of length l in the rectangle so far. Partial height is 
# k. Then all we have to check is if these partial columns are prefixes
# for valid words of height h. If they are, then we try appending
# new words of length l to grow the rectangle until we have words left.
# If we find any prefix to be invalid, we return immediately. We repeat
# this until we find all columns of height h to be valid.

# Thats the basic idea of the problem!
