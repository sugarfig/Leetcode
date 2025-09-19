class Solution:
    # first check if lengths match
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapString1 = {}
        mapString2 = {}

        # for char1 in s:
        #     if char in mapString1:
        #         mapString1[char] += 1
        #     else:
        #         mapString1[char] = 1
        
        # for char in t:
        #     if char in mapString2:
        #         mapString2[char] += 1
        #     else:
        #         mapString2[char] = 1

        for char1, char2 in zip(s, t):
            mapString1[char1] = mapString1.get(char1, 0) + 1
            mapString2[char2] = mapString2.get(char2, 0) + 1

        # if len(mapString1) != len(mapString2):
        #     return False
        
        return mapString1 == mapString2