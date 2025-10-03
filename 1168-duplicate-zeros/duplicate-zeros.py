class Solution:
    # go thru twice
    # first time get the amount of zeros in it before we reach the max amount of spaces in the array
    # then that amount will basically be the amount that we "chop" off the end
    # if last is a 0 before got chopped then just put that at the end of the array
    # start from end of array
    # if index value is 0 then put a 0 at current count + index value
    # subtract one from count then put another zero at count + index
    # otherwise just put value at current index at index + count
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count = 0
        length = len(arr) - 1
        for index in range(length + 1):
            if index > length - count:
                break
            if arr[index] == 0:
                if index == length - count:
                    arr[length] = 0
                    length -= 1
                    break
                count += 1
        # print(count)
        last = length - count
        
        for index in range(last, -1, -1):
            # print(arr[index]) 
            # print(count) 
            if arr[index] == 0:
                arr[index + count] = 0
                count -= 1
                arr[index + count] = 0
            else:
                arr[index + count] = arr[index]