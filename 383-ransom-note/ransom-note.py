class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magHash = {}
        ransomHash = {}

        for char in ransomNote:
            ransomHash[char] = ransomHash.get(char, 0) + 1
        for char in magazine:
            magHash[char] = magHash.get(char, 0) + 1
        
        for i in ransomHash:
            if ransomHash[i] > magHash.get(i, 0):
                return False

        return True