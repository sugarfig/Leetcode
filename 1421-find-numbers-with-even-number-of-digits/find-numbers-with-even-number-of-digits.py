class Solution:
    # do a for loop to go thru nums and make num string and get the length of the string
    # if modulus of length == 0 then add to count
    # return count
    def findNumbers(self, nums: List[int]) -> int:
        evenNumbersCount = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                evenNumbersCount += 1
                
        return evenNumbersCount