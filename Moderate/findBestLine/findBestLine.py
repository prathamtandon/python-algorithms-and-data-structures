# Given a 2-D graph with points on it, find the line which passes the
# most number of points.

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line:
    def __init__(self,p,q):
        self.epsilon = 10e-4
        self.slope = -1
        self.intercept = -1
        self.infinite_slope = False

        if abs(p.x - q.x) > self.epsilon:
            self.slope = (float(p.y)-q.y)/(p.x-q.x)
            self.intercept = p.y-self.slope*p.x
        else:
            self.infinite_slope = True
            self.intercept = p.x

    def floorToNearestEpsilon(self,d):
        r = int(d/self.epsilon)
        return (float(r))*self.epsilon

    def isEquivalent(self,a,b):
        return abs(a-b) < self.epsilon

    def isEquivalent_line(self,other):
        if self.isEquivalent(self.slope,other.slope) and self.isEquivalent(self.intercept,other.intercept) and self.infinite_slope == other.infinite_slope:
            return True
        return False

# Find line that goes through most number of points
def findBestLine(points):
    linesBySlope = getListOfLines(points)
    return getBestLine(linesBySlope)

# Add each pair of points as a line to the list
def getListOfLines(points):
    linesBySlope = {}
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            line = Line(points[i],points[j])
            key = line.floorToNearestEpsilon(line.slope)
            if key in linesBySlope:
                linesBySlope[key].append(line)
            else:
                linesBySlope[key] = [line]

    return linesBySlope

# Return the line with the most equivalent other lines
def getBestLine(linesBySlope):
    bestLine = None
    bestCount = 0

    for slope in linesBySlope:
        lines = linesBySlope[slope]
        for line in lines:
            # count the lines that are equivalent to current line
            count = countEquivalentLines(linesBySlope,line)

            if count > bestCount:
                bestLine = line
                bestCount = count

    return bestLine

def countEquivalentLines(linesBySlope,line):
    key = line.floorToNearestEpsilon(line.slope)
    count = countEquivalentLines_helper(linesBySlope[key],line)
    if key+line.epsilon in linesBySlope:
        count += countEquivalentLines_helper(linesBySlope[key+line.epsilon],line)
    if key-line.epsilon in linesBySlope:
        count += countEquivalentLines_helper(linesBySlope[key-line.epsilon],line)
    return count

def countEquivalentLines_helper(listOflines, line):
    if listOflines is None:
        return 0

    count = 0
    for parallelLine in listOflines:
        if parallelLine.isEquivalent_line(line):
            count += 1

    return count

