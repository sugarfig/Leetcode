# class Solution:
#     def duplicateZeros(self, arr: List[int]) -> None:
#         """
#         Do not return anything, modify arr in-place instead.
#         """
#         count = 0
#         for index in range(len(arr)):
#             if index > len(arr) - 1 - count:
#                 break
#             if arr[index] == 0:
#                 # if index == len(arr) - 1 - count:
#                 #     arr[-1] = 0
#                 #     count -= 1
#                 #     break
#                 count += 1
#         # print(count)
#         last = len(arr) - 1 - count
        
#         for index in range(last, -1, -1):
#             # print(arr[index]) 
#             # print(count) 
#             if arr[index] == 0:
#                 arr[index + count] = 0
#                 count -= 1
#                 arr[index + count] = 0
#             else:
#                 arr[index + count] = arr[index]


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        possible_dups = 0
        length_ = len(arr) - 1

        # Find the number of zeros to be duplicated
        for left in range(length_ + 1):

            # Stop when left points beyond the last element in the original list
            # which would be part of the modified list
            if left > length_ - possible_dups:
                break

            # Count the zeros
            if arr[left] == 0:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as left is pointing to the last element which could be included  
                if left == length_ - possible_dups:
                    arr[length_] = 0 # For this zero we just copy it without duplication.
                    length_ -= 1
                    break
                possible_dups += 1

        # Start backwards from the last element which would be part of new list.
        last = length_ - possible_dups

        # Copy zero twice, and non zero once.
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]