# Given a list of sorted strings interspersed with empty strings, write
# a method to return location of a given string.

# The main idea is to find a non-empty string as mid and then do a
# bin-search in left or right halves.

def search(strings, x, low, high):
    if low > high:
        return -1
    mid = (low + high)/2

    if strings[mid] == "":
        left = mid-1
        right = mid+1

        while True:
            if left < low and right > high:
                return -1
            elif right <= high and strings[right] != "":
                mid = right
                break
            elif left >= low and strings[left] != "":
                mid = left
                break
            left -= 1
            right += 1

    if strings[mid] == x:
        return mid
    elif strings[mid] > x:
        return search(strings, x, low, mid-1)
    else:
        return search(strings, x, mid+1, high)


def sparseSearch(strings, x):
    if x is None or x == "":
        return -1
    return search(strings, x, 0, len(strings)-1)
