class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        a = 0
        b = len(s) - 1

        while a < b:
            print(b)
            tempChar = s[b]
            s[b] = s[a]
            s[a] = tempChar
            b = b - 1
            a = a + 1

        return s

