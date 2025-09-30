class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) < 0:
            return []

        # result = []
        # result.append(nums[0])
        # for i in range(1, len(nums)):
        #     result.append(result[i - 1] + nums[i])
        # return result

        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        return nums