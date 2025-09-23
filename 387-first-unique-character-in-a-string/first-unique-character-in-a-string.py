class Solution:
    # count all the chars in the string s and add this to the hashmap and have the char be the key and the amount of times it shows up the value
    # loop thru the string s again and find each character in the hashmap and if the value for that character is greater than 1, then keep going and if not it is equal to 1 then return that index
    # if the for loop finishes without returning any index, then return -1
    # September 23, 2025 #16
    def firstUniqChar(self, s: str) -> int:
        charMap = {}
        for char in s:
            if char in charMap:
                charMap[char] += 1
            else:
                charMap[char] = 1
        for index, char in enumerate(s):
            value = charMap[char]
            if value == 1:
                return index
        return -1