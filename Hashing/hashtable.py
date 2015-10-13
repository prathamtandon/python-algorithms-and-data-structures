# Implementing a hashtable from scratch.

# The implementation uses the multiplication method
# (https://www.cs.auckland.ac.nz/software/AlgAnim/hash_func.html) to
# create a hash function. Collisions are resolved using chaining.
# Assumption is that keys are natural numbers {1,2,...,N}. For
# character strings, we represent as a radix-128 integer.

# Let p = 14; w(word size) = 32; size of table, m = 2^p = 2^14
# We define A to be a fraction of the form s/pow(2,32) which is
# closest to (sqrt(5)-1)/2.
# Define s = A.pow(2,32)
# Multiply s with key, k to get a result of size 2w bits.
# Take the lower order w bits. Return the most significant p bits
# from these w bits as the hash value.
from math import sqrt
from math import floor

p = 14
w = 32
A = (sqrt(5)-1)/2
m = pow(2, p)
radix = 128

def get_hash(key):
    return int(floor(m * (key * A % 1)))

def string_to_int(string):
    str_len = len(string)
    result = 0

    for i in reversed(range(0,str_len)):
        result += ord(string[i]) * pow(radix, str_len-i-1)

    return result

class HashTable:
    def __init__(self):
        self.table = [None]*m
        self.table_size = 0

    def get_slot_index(self, key):
        slot_index = -1
        if isinstance(key, str):
            slot_index = get_hash(string_to_int(key))
        else:
            slot_index = get_hash(key)
        return slot_index

    def put(self, key, value):
        slot_index = self.get_slot_index(key)

        if self.table[slot_index] is None:
            self.table[slot_index] = []

        lst = self.table[slot_index]
        is_update = False

        for i in range(len(lst)):
            if lst[i][0] == key:
                lst[i][1] = value
                is_update = True
                break

        if not is_update:
            self.table[slot_index].insert(0, (key, value))
            self.table_size += 1

    def get(self, key):
        slot_index = self.get_slot_index(key)

        if self.table[slot_index] is None:
            return None

        lst = self.table[slot_index]

        for i in range(len(lst)):
            if lst[i][0] == key:
                return lst[i][1]

        return None


    def remove(self, key):
        slot_index = self.get_slot_index(key)

        if self.table[slot_index] is None:
            return

        lst = self.table[slot_index]
        index = -1

        for i in range(len(lst)):
            if lst[i][0] == key:
                index = i
                break

        if index != -1:
            self.table[slot_index].pop(index)
            self.table_size -= 1


    def size(self):
        return self.table_size

