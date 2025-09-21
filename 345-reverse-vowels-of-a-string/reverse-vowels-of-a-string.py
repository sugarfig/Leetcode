class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        a = 0
        b = len(s) - 1

        while a < b:
        #    if (s[a] == 'a' or s[a] == 'e' or s[a] == 'i' or s[a] == 'o' or s[a] == 'u') and (s[b] == 'a' or s[b] == 'e' or s[b] == 'i' or s[b] == 'o' or s[b] == 'u'):
            if s[a] in 'aeiouAEIOU' and s[b] in 'aeiouAEIOU':
                s[a], s[b] = s[b], s[a]
                a = a + 1
                b = b - 1
            if s[a] not in 'aeiouAEIOU':
                a = a + 1
            if s[b] not in 'aeiouAEIOU':
                b = b - 1
        return "".join(s)

        