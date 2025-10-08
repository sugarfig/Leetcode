class Solution:
    # check that array is at least length of 3
    # find the largestIndex. this will be the peak, but also check that it is not the first or last index. if it is, then return False
    # set a boolean to false and begin to loop thru arr from beginning up until largestIndex. if all values before largest array are smaller than each other bool var is true if any is not, then just return False
    # now loop thru 2nd half of arr with beginning at the largestIndex + 1 to the end of the array and again check that the values are smaller than the one before and if one is not, then return false.
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        # largest = arr[0]
        largestIndex = 0
        for i in range(1, len(arr)):
            if arr[largestIndex] < arr[i]:
                largestIndex = i
            if largestIndex == 0 or largestIndex == len(arr) - 1:
                print("output false here")
                return False
        print(largestIndex)
        isMountain = False
        pointer1 = 1

        for i in range(largestIndex):
            if arr[i] < arr[pointer1]:
                isMountain = True
                pointer1 += 1
            else:
                print("output false here1")
                return False

        pointer2 = largestIndex
        for i in range(largestIndex + 1, len(arr)):
            print(arr[i], "-> arr[i]")
            print(arr[pointer2], "-> arr[pointer2]")
            if arr[i] < arr[pointer2]:
                isMountain = True
                pointer2 += 1
            else:
                print("output false here2")
                return False
        
        # for i in range(len(arr)):
        #     if i < largestIndex and arr[pointer1] < arr[pointer2]:
        #         return True
        #     if i > largestIndex and arr[pointer1] > arr[pointer2]:
        #         return True
        #     pointer1 += 1
        #     pointer2 += 1
        return isMountain
            