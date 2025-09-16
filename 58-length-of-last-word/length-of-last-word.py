class Solution:
# loops thru from the back
# have a bool that turns "on" when the char is a char and off when at a whitespace
# have a counter that counts the amount fo spaces that are currently being incrememnted while bool is off
# reuturn counter as soon as previous bool is "on" and current bool is off or if reached length of entire string s
    def lengthOfLastWord(self, s: str) -> int:
        isChar = False
        count = 0
        isPreviousChar = False
        for char in reversed(s):
            isPreviousChar = isChar
            if char.isalpha():
                isChar = True
                count = count + 1
            else:
                isChar = False
            
            if isPreviousChar == True and isChar == False :
                return count

        return count

        