# Accepts two strings and returns true if they are one or zero edits
# away.
# EXAMPLE
# pale, ple => true
# pales, pale => true
# pale, bale => true
# pale, bake => false


def OneAway(str1, str2):
	if (abs(len(str1) - len(str2)) >= 2):
		return False
	found_difference = False
	shorter = str2 if len(str1) > len(str2) else str1
	longer = str1 if shorter == str2 else str2
	longer_index = 0
	shorter_index = 0
	while shorter_index < len(shorter) and longer_index < len(longer):
		if shorter[shorter_index] is not longer[longer_index]:
			if found_difference is True:
				return False
			found_difference = True
			if len(shorter) < len(longer):
				longer_index += 1
		longer_index += 1
		shorter_index += 1
			
	return True
