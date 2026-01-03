class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # loop for shortest word times 2 cause we are gonna alternate with the other word.
        # alternate and keep bool to track which word we are on.
        # once done with shortest word. append the rest of the other word to result string.

        shortestWord = ""
        word1Go = True
        result = ""
        word1Counter = 0
        word2Counter = 0

        if len(word1) < len(word2):
            shortestWord = word1
        else:
            shortestWord = word2
        
        for count in range(len(shortestWord)*2):
            if word1Go:
                result = result + word1[word1Counter]
                word1Counter+= 1
                word1Go = False
            else:
                result = result + word2[word2Counter]
                word2Counter+=1
                word1Go = True

        if word1 == shortestWord:
            result = result + word2[word2Counter:]
        else:
            result = result + word1[word1Counter:]
        
        return result
        