# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        # result: Optional[ListNode]
        result = ListNode()
        resultTemp = result
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                # print(curr1)
                resultTemp.next = curr1
                print(resultTemp)
                print(result)
                resultTemp = resultTemp.next
                # print(resultTemp.val)
                curr1 = curr1.next
            else:
                # print(curr2.val)
                resultTemp.next = curr2
                print(resultTemp.val)
                resultTemp = resultTemp.next
                curr2 = curr2.next
        if curr1 == None:
            resultTemp.next = curr2
        elif curr2 == None:
            resultTemp.next = curr1

        return result.next
            # if curr1.val <= curr2.val:
            #     result = curr1
            # else:
            #     result = curr2

