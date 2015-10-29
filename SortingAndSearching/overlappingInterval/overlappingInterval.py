# Given a list of intervals, find the interval which overlaps
# with the maximum number of intervals and the number of overlaps.

# 1. Sort the intervals while marking each value as start or end.
# 2. Repeat for each interval
#      (a) If start interval, increment count. Compare count and max_count,
#          update if needed and set overlap.start = start. Set a flag
#      (b) If end interval, decrement count. If flag is set(which means
#          we haven't found an end for current optimal), then set overlap.end = end
#          and reset flag.

class Interval:
    def __init__(self, low, high):
        self.low = low
        self.high = high

class IntervalHelper:
    def __init__(self, key, is_low):
        self.key = key
        self.is_low = is_low

def transformIntervals(intervals):
    transformed = []
    for interval in intervals:
        low = IntervalHelper(interval.low, True)
        high = IntervalHelper(interval.high, False)
        transformed.append(low)
        transformed.append(high)

    return transformed

def intervalComparator(int1, int2):
    if int1.key < int2.key:
        return -1
    elif int1.key == int2.key:
        return 0
    else:
        return 1

def overlappingInterval(intervals):
    transformed = transformIntervals(intervals)
    transformed = sorted(transformed, cmp=intervalComparator)

    max_count = -float('inf')
    count = 0
    overlap = Interval(0,0)
    flag = 0

    for interval in transformed:
        if interval.is_low:
            count += 1
            if count > max_count:
                max_count = count
                overlap.low = interval.key
                flag = 1
        else:
            count -= 1
            if flag == 1:
                overlap.high = interval.key
            flag = 0

    return overlap
