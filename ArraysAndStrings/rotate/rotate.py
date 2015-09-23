# Given an image represented by an NxN matrix, where each pixel in
# image is 4 bytes, rotates the image by 90 degrees.

# NOTE: The solution becomes much more clear when we take an
# actual matrix and run multiple iterations to swap by-hand.

def rotate_image(matrix, N):
	# layers move from outermost to innermost
    for layer in range(N/2):
        first = layer
        last = N - layer - 1
        # Scan from 0...N-1, 1...N-2, ... N/2
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last-offset][first]
            matrix[last-offset][first] = matrix[last][last-offset]
            matrix[last][last-offset] = matrix[i][last]
            matrix[i][last] = top
