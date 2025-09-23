class Solution:
    # use build in function (.find)
    # this function returns the index of the first letter of the first instance of that string and if not found, returns -1
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)