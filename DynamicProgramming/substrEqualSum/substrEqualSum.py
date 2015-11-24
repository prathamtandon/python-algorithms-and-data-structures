# Given a string 'str' of digits, find the length of the longest
# substring of 'str', such that length of substring is 2k and sum
# of left k digits is equal to sum of right k digits.

def substrEqualSum (string):
    if len(string) == 0:
        return 0
    
    result = 0
    for i in range(len(string)-1):
        print i
        left = i
        right = i+1
        left_sum = 0
        right_sum = 0
        while left >= 0 and right < len(string):
            left_sum += int(string[left])
            right_sum += int(string[right])
            if left_sum == right_sum:
                result = max(result, right-left+1)
            left -= 1
            right += 1
        
    return result
                 
