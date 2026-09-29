class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # sort the array
        # edge cases are 0 in the begining and last one
        # make sure 0th index is 0 and then start at 1 and if current is 1 + prev then good and continue looping
        # if current is not then return the 1 + prev.
        # if/when loop finishes, return 1 + last index

        nums.sort()

        if nums[0] != 0:
            return 0
        
        for num in range(1, len(nums)):
            if nums[num] != nums[num - 1] + 1:
                return nums[num - 1] + 1

        return nums[len(nums) - 1] + 1


        