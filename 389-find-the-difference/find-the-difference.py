class Solution:

    def findTheDifference(self, s: str, t: str) -> str:
        differenceChar = ""
        hash1 = {}
        hash2 = {}
        # charSet = set(t) - set(s)
        # print(charSet)

        # if len(charSet) > 0:
        #    return charSet.pop()

        # return ""
        # return (set(t) - set(s)).pop()
        if len(t) <= 0:
            return ""

        for char1, char2 in zip(s,t):
            hash1[char1] = hash1.get(char1, 0) + 1
            hash2[char2] = hash2.get(char2, 0) + 1
        
        hash2[t[len(t) - 1]] = hash2.get(t[len(t) - 1], 0) + 1

        differenceChar = hash2.keys() - hash1.keys()
        if len(differenceChar) > 0:
            return differenceChar.pop()

        differenceChar = {k: hash1[k] for k in hash1 if k in hash2 and hash1[k] != hash2[k]}
        key, value = differenceChar.popitem()
        return key

        # return ""
        
