# Basic string compression.
# EXAMPLE
# Input aabcccccaaa
# Output a2b1c5a3
# If the "compressed" string would not become smaller than the original,
# return the original string

def compress(original):
    compressed_list = []
    consecutive_count = 0

    for i in range(len(original)):
        consecutive_count += 1
        if i + 1 >= len(original) or original[i] != original[i + 1]:
            compressed_list.append(original[i])
            compressed_list.append(str(consecutive_count))
            consecutive_count = 0

    compressed_string = ''.join(compressed_list)
    return compressed_string if len(compressed_string) < len(original) else original
