class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        min = 0
        max = len(nums)-1
        mid = (min + max) //2
        while min <= max:
            val = nums[mid]
            if target == val:
                return mid
            if target < val:
                max = mid-1
            else:
                min = mid+1
            mid = (min + max) //2
        return min
            