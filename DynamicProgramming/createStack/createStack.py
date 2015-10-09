# Given stack of n boxes, with widths w(i), heights h(i) and 
# depth d(i). The boxes can only be stacked on top of each other
# if each box in the stack is strictly larger than the box above it
# in all three dimensions. Find height of tallest possible stack.
# Height of stack is the sum of heights of each box.

class Box:
	def __init__(self, w, h, d):
		self.w = w
		self.h = h
		self.d = d
		
	def __eq__(self, other):
		return self.h - other.h
	
	def canBeAbove(self, other):
		return self.w > other.w and self.h > other.h and self.d > other.d

# Check the height of tallest stack that can be formed by having
# box 1 at bottom, box 2 at bottom, box 3 at bottom ... box n at bottom.
# Then at one level above, again check the height of tallest stack
# formed using all remaining boxes once as the bottom and so on.

# Here, heightMap[i] represents the tallest stack height with box i
# at bottom.

def createStack(boxes):
	# sort in descending order of height
	sorted(boxes)
	maxHeight = 0
	heightMap = [0]*len(boxes)
	for i in range(len(boxes)):
		height = createStack_helper(boxes, i, heightMap)
		maxHeight = max(height, maxHeight)
	return maxHeight

def createStack_helper(boxes, bottomIndex, heightMap):
	if bottomIndex < len(boxes) and heightMap[bottomIndex] > 0:
		return heightMap[bottomIndex]
	bottom = boxes[bottomIndex]
	maxHeight = 0
	for i in range(bottomIndex+1, len(boxes)):
		if boxes[i].canBeAbove(bottom):
			height = createStack_helper(boxes, i)
			maxHeight = max(height, maxHeight)
	maxHeight += bottom.h
	heightMap[bottomIndex] = maxHeight
	return maxHeight
			
# Method 2: We chose whether or not put box 0 on the stack.
# Take one recursive path with box 0 at the bottom, and one
# one without box 0. Return the better of the two options.
# Then we chose whether we put box 1 in the stack. Take two
# recursive paths and return the better of the two.

def createStack2(boxes):
	sorted(boxes)
	heightMap = [0]*len(boxes)
	createStack_helper2(boxes, None, 0, heightMap)

def createStack_helper2(boxes, bottom, offset, heightMap):
	if offset >= len(boxes):
		return 0
	newBottom = boxes[offset]
	heightWithBottom = 0
	if(bottom is None or newBottom.canBeAbove(bottom)):
		if heightMap[offset] == 0:
			heightMap[offset] = createStack_helper2(boxes, newBottom, offset+1, heightMap)
			heightMap[offset] += newBottom.h
		heightWithBottom = heightMap[offset]
	
	heightWithoutBottom = createStack_helper2(boxes, bottom, offset+1, heightMap)
	
	return max(heightWithBottom, heightWithoutBottom)
