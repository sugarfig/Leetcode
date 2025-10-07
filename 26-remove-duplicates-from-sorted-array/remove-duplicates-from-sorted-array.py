class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        reader = 1
        writer = 0

        while reader < len(nums):
            if nums[reader] != nums[writer]:
                writer += 1
                nums[writer] = nums[reader]
                # writer += 1
            reader += 1
        print(writer)
        emptySpaces = len(nums) - writer
        for i in range(emptySpaces - 1):
            nums.pop()