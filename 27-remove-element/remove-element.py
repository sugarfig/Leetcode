class Solution:
    # count thru all the target values first to see how many we will need to pop in the end
    # while the beg pointer is less than the end pointer,
    # check if the end index val is equal to val. if so, then subtract an index value from end
    # if beginning value is equal to val then swap and then subtract from end
    # otherwise add to beggining pointer
    # loop thru the count and pop all the unnecessary values
    def removeElement(self, nums: List[int], val: int) -> int:
        
        begIndex = 0
        endIndex = len(nums) - 1
        count = 0
        
        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
        # if len(nums) <= 0:
        #     return
        while begIndex < endIndex:
            if nums[endIndex] == val:
                endIndex -= 1
                # count += 1
            if nums[begIndex] == val:
                # count += 1
                # print(nums[begIndex])
                nums[begIndex], nums[endIndex] = nums[endIndex], nums[begIndex]
                # print(nums[begIndex])
                endIndex -= 1 
            else: 
                begIndex += 1
            # endIndex -= 1
        # print(count)
        # if count == 0:
        #     nums.pop()
        for c in range(count):
            nums.pop()