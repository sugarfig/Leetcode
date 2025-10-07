class Solution:
    # have 2 pointers. one will be a reader. the other will be a writer. reader will start at index 1 and writer will start at index 0
    # we have a while loop so while reader is not at the end of the array
    # if the value at reader and writer are not equal, then increment writer and then put val at reader to writer
    # add 1 to reader every loop
    # after loop is done, get the amount of indicies we need to pop from nums by doing lens of nums minus writer which is at the largest index that does not reapeat any vals
    # then loop thru that number and pop that many times
    def removeDuplicates(self, nums: List[int]) -> int:
        reader = 1
        writer = 0

        while reader < len(nums):
            if nums[reader] != nums[writer]:
                writer += 1
                nums[writer] = nums[reader]
                # writer += 1
            reader += 1
        # print(writer)
        emptySpaces = len(nums) - writer
        for i in range(emptySpaces - 1):
            nums.pop()