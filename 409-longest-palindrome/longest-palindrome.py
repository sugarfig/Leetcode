class Solution:
    # if length is 1, that is the longest palindrome
    # create a hashmap and count how many times a specific character appears in the string
    # loop thru the hashmap and check if the value in the hashmap is 2 or over
    # if it is, then add how many pairs it has to a counter called pairs
    # if not, don't do anything
    # result will be the amount of pairs times 2
    # if the length of the string is less than the amount in result then add 1
    # return result
    # September 23, 2025 #19
    def longestPalindrome(self, s: str) -> int:
        pairs = 0
        charMap = {}
        if len(s) == 1:
            return 1
        for char in s:
            charMap[char] = charMap.get(char, 0) + 1
        
        for key, value in charMap.items():
            # if value >= 2:
            #    pairs = pairs + math.floor(value / 2)
            if value % 2 == 0:
                pairs = pairs + value
            else:
                pairs = pairs + (value - 1)
            
        # result = pairs * 2
        if pairs < len(s):
            return int(pairs + 1)

        return int(pairs)