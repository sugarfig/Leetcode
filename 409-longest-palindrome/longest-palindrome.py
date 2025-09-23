class Solution:
    # create a hashmap and count how many times a specific character appears in the string
    def longestPalindrome(self, s: str) -> int:
        pairs = 0
        charMap = {}
        if len(s) == 1:
            return 1
        for char in s:
            charMap[char] = charMap.get(char, 0) + 1
        
        for key, value in charMap.items():
            if value >= 2:
               pairs = pairs + math.floor(value / 2)
            
        result = pairs * 2
        if result < len(s):
            return int(result + 1)

        return int(result)