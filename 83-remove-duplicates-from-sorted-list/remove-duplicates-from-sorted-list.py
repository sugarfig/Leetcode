# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if curr == None or curr.next == None:
            return head
        nextCurr = curr.next
        print(nextCurr)

        while curr and nextCurr:
            if curr.val == nextCurr.val:
                curr.next = nextCurr.next
            else:
                curr = curr.next
            nextCurr = nextCurr.next
            # else:
            #     curr = curr.next
        return head

        