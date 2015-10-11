# Write a method to sort an array of strings so that all anagrams are
# next to each other.

# Method 1: Define a custom comparator that returns 0 if two
# strings are anagrams of each other. We then use this comparator
# for sorting strings.

def make_comparator(less_than):
    def compare(x, y):
        return less_than(x, y)
    return compare

def anagram_comparator(x, y):
    sorted_x = "".join(sorted(x))
    sorted_y = "".join(sorted(y))

    print "x: " + x
    print "y: " + y

    if sorted_x == sorted_y:
        print 'Equal'
        print 'sorted_x:' + str(sorted_x)
        print 'sorted_y:' + str(sorted_y)
        print '\n'

        return 0
    elif x > y:
        print 'Greater'
        print '\n'

        return 1
    else:
        print 'Lesser'
        print '\n'
        return -1

def sortAnagrams(array):
    return sorted(array, cmp=make_comparator(anagram_comparator))


# Method 2: Use Hash table. For each string in input array, add
# string to a Hash table with key as sorted value for that string.
# This means that all strings which are anagrams would be sorted to
# same slot. Then go through all values in the Hash table and
# add them to an output array.

def sortAnagrams2(array):
    hashmap = {}
    for string in array:
        key = "".join(sorted(string))
        if key in hashmap:
            hashmap[key].append(string)
        else:
            hashmap[key] = [string]

    array = []
    for key in hashmap:
        array += hashmap[key]

    return array
