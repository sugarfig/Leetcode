class Solution:
    # have 2 variables keeping track of indicies of 1st and 2nd array
    # loop while the 2nd array has not been iterated thru all the way
    # if the length of array1 is less than the index1 and value in array2 is less than or equal to the value in array1 then insert that value and pop from array1 and increment both index1 and index2 and the current length of array1. currenlength is used to keep track of current indicies occupied of array1
    # if index1 is less than the currentlength then add 1 to index1
    # otherwise replace whatever is in the index2. increment length bc added to array1 and also increment to index2 bc already used taht index
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        currLen = m
        indexNums2 = 0
        indexNums1 = 0
        
        while indexNums2 < n :
            # print("index2", nums2[indexNums2])
            # print("index1", nums1[indexNums1])
            if indexNums1 < currLen and nums2[indexNums2] <= nums1[indexNums1]:
                nums1.insert(indexNums1, nums2[indexNums2])
                nums1.pop()
                indexNums1 += 1
                indexNums2 += 1
                currLen += 1
                
            elif indexNums1 < currLen:
                indexNums1 += 1
            else:
                print(indexNums2)
                # nums1.insert(m + indexNums2, nums2[indexNums2])
                # nums1.pop()
                nums1[currLen] = nums2[indexNums2]
                # indexNums2 += 1
                currLen += 1
                indexNums2 += 1
            # else:
            #     indexNums1 += 1
                
            