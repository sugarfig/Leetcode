# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # create 2 pointers that point to beginning of list1 and list2. these will be used to iterate thru the lists
    # then create 1 node and a pointer that also points to the beginning of this list which in the beginning is just the node
    # loop thru list1 and list2 using curr1 and curr2 until one list ends and compare which one is smaller and make the result pointer/iterator.next point to the new node that is smaller
    # once one list ends (gets to none), just add the other list that did not end yet set to the result pointer/iterator.next
    # return result.next bc the first node was just a dummy one, we actually wanted the first one that gets set which is found with .next
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

