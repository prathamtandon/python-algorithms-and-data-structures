# Accepts two strings and returns if one is rotation of another
# EXAMPLE "waterbottle" is rotation of "erbottlewat"

def isRotation(str1, str2):
    if len(str1) == len(str2) and len(str1) > 0:
        str1str1 = ''.join([str1, str1])
        return str1str1.find(str2) >= 0
    return False
