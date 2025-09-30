class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # go thru nums and start at 1 to end of nums. add nums at index i - 1 to nums at index i then replace nums at index i
        # ORRR append nums at index 0 to result
        # go thru nums and start at 1 to end of nums. 
        # add value at index i - 1 in result to nums at index i then append to result
        
        if len(nums) < 0:
            return []
        # this works too, but rewrote without needing the results array
        # result = []
        # result.append(nums[0])
        # for i in range(1, len(nums)):
        #     result.append(result[i - 1] + nums[i])
        # return result

        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        return nums