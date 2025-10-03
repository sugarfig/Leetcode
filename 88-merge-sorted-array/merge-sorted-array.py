# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         valid_end = m
#         indexNums2 = 0
#         indexNums1 = 0
        
#         while indexNums2 < n :
#             # print("index2", nums2[indexNums2])
#             # print("index1", nums1[indexNums1])
#             if indexNums1 < valid_end and nums2[indexNums2] <= nums1[indexNums1]:
#                 nums1.insert(indexNums1, nums2[indexNums2])
#                 nums1.pop()
#                 indexNums1 += 1
#                 indexNums2 += 1
#                 valid_end += 1
                
#             elif indexNums1 < m:
#                 indexNums1 += 1
#             else:
#                 print(indexNums2)
#                 nums1.insert(m + indexNums2, nums2[indexNums2])
#                 nums1.pop()
#                 indexNums2 += 1
#                 indexNums1 += 1
#             # else:
#             #     indexNums1 += 1
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        indexNums1 = 0
        indexNums2 = 0
        currLen = m  # current number of valid elements in nums1

        while indexNums2 < n:
            # If we haven't reached the end of the valid part of nums1
            if indexNums1 < currLen and nums2[indexNums2] <= nums1[indexNums1]:
                nums1.insert(indexNums1, nums2[indexNums2])
                nums1.pop()  # keep length constant
                indexNums1 += 1
                indexNums2 += 1
                currLen += 1  # valid region grows
            elif indexNums1 < currLen:
                # current nums2[indexNums2] is bigger than nums1[indexNums1], move forward
                indexNums1 += 1
            else:
                # reached the end of the valid region, place nums2[indexNums2] at the end
                nums1[currLen] = nums2[indexNums2]
                currLen += 1
                indexNums2 += 1

            