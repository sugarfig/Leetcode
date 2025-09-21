class Solution:
    # create a stack and take out all the special characters and spaces in original string. also put everything to lower case
    # loop thru string and put into a stack
    # loop thru stack (cant use for loop cause that modifies actual list. see comment below) then create a new string with the popped items from the stack.
    # return the comparison between thr new string created and the string given
    def isPalindrome(self, s: str) -> bool:
        palindromeCheckStack = []
        reverseString = ""
        # count = 0
        s = "".join(char for char in s if char.isalnum()).lower()

        # print(s)

        for char in s:
            palindromeCheckStack.append(char)
            # print(char)
        # print(palindromeCheckStack)

        # for char in palindromeCheckStack: // not able to do this bc modifies the actual list and not a copy so only half will get looped thru bc indicies get messed up since modifying the original
        while palindromeCheckStack:
            # print(palindromeCheckStack.pop())
            # print(reverseString)
            # print(count)
            # count = count + 1
            reverseString = reverseString + palindromeCheckStack.pop()


        # print(reverseString)
        # print(s)
        return reverseString == s