class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dictionary = {}
        # result = []

        for num in nums:
            # print(num)
            dictionary[num] = 0;
        
        nums.clear()
        for key in dictionary:
            # return key
            print(key)
            nums.append(key)
            # nums[:] = list(range(key + 1))

        return len(nums)

        