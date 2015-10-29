from overlappingInterval import Interval, overlappingInterval

def test_overlappingInterval():
    intervals = [Interval(1990,2013),Interval(1995,2000),Interval(2010,2020),Interval(1992,1999)]

    res = overlappingInterval(intervals)
    assert(res.low == 1995)
    assert(res.high == 1999)

    intervals = [Interval(6,10), Interval(9,12), Interval(4,11)]

    res = overlappingInterval(intervals)
    assert(res.low == 9)
    assert(res.high == 10)
