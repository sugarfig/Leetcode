class Solution:
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