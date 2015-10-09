# Paint fill : Given a screen (represented by a 2-d array of colors),
# a point, and a new color, fill in the surrounding area until the color
# changes from the original color.

from enum import Enum

class Color(Enum):
	BLACK = 1
	WHITE = 2
	RED = 3
	YELLOW = 4
	GREEN = 5

def PaintFill(screen, r, c, nColor):
	if screen[r][c] == nColor:
		return False
	return PaintFill_helper(screen, r, c, screen[r][c], nColor)

def PaintFill_helper(screen, r, c, oColor, nColor):
	if r < 0 or r >= len(screen) or c < 0 or c >= len(screen[0]):
		return False
	if screen[r][c] == oColor:
		PaintFill_helper(screen, r-1, c, oColor, nColor)
		PaintFill_helper(screen, r+1, c, oColor, nColor)
		PaintFill_helper(screen, r, c-1, oColor, nColor)
		PaintFill_helper(screen, r, c+1, oColor, nColor)
	return True
