class Solution:
    # go thru num in nums and if num is 1, add to ones
    # if not, set consecutive nums back to 0
    # if highest number is less than consecutive ones then set consecutive ones to highest number
    # return highest number after for loop is done
    
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutiveOnes = 0
        highestNumber = 0
        
        for num in nums:
            if num == 1:
                consecutiveOnes += 1
            else:
                consecutiveOnes = 0
            if highestNumber <= consecutiveOnes:
                highestNumber = consecutiveOnes
                
        return highestNumber