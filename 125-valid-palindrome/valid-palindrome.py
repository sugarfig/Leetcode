class Solution:

    def isPalindrome(self, s: str) -> bool:
        palindromeCheckStack = []
        reverseString = ""
        count = 0
        s = "".join(char for char in s if char.isalnum()).lower()

        # print(s)

        for char in s:
            palindromeCheckStack.append(char)
            # print(char)
        # print(palindromeCheckStack)

        while palindromeCheckStack:
            # print(palindromeCheckStack.pop())
            # print(reverseString)
            # print(count)
            count = count + 1
            reverseString = reverseString + palindromeCheckStack.pop()


        # print(reverseString)
        # print(s)
        return reverseString == s