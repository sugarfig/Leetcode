class Solution:
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
                
            