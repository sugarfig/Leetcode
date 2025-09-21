class Solution:
    # check to see if t is empty. if it is, return nothing
    # create 2 hashmaps. with the keys being the chars in the strings and the values being the amount of times that char appears in that string
    # the 2nd string (string t) will always have one more char than the 1st string (string s) so once we are done looping thru both, we still have to assign the last char from string t to hash2
    # now we can check to see if there is a difference in they keys first in the maps and if no difference in keys then it will check the values to see if there could just be a duplicate of a letter added.
    # once it does this, it will return key and value of the difference with popitem()
    # then we can just return the key
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

        # differenceChar = hash2.keys() - hash1.keys()
        # if len(differenceChar) > 0:
        #     return differenceChar.pop()

        differenceChar = {k: hash2[k] for k in hash2 if (k not in hash1) or (k in hash1 and hash1[k] != hash2[k])}
        key, value = differenceChar.popitem()
        return key

        # return ""
        
