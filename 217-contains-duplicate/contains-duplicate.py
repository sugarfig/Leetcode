class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # loop thru array
        # build hashmap and have count be value and key be the num in array so we have o(1) lookup
        # if we find continue to look thru array and find a value that already in hashmap, we can just return True 
        # otherwise return false

        # nums_map = defaultdict(int)

        # for num in nums:
        #     nums_map[num] += 1

        #     if nums_map[num] == 2:
        #         return True

        # return False

        # faster:
        # sort then check if the current is the same as the next. if yes then return true.

        nums.sort()

        for num in range(len(nums) - 1):
            if nums[num] == nums[num + 1]:
                return True
        return False