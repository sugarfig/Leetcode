# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # have 2 pointers one that points at head at first and another that points to next
    # need to check if empty and if only one node. if either of these, then just return head
    # if not, then create nextCurr
    # loop until nextCurr become none
    # if curr.val is equal to nextCurr.val then have current next point to nextCurr next (not to nextCurr because those 2 are the same)
    # if not equal then just move curr to the next one
    # always move nextCurr by one
    # keep looping until nextCurr becomes none
    # return head bc this is what we rearranged/deleted from
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if curr == None or curr.next == None:
            return head
        nextCurr = curr.next
        print(nextCurr)

        while nextCurr:
            if curr.val == nextCurr.val:
                curr.next = nextCurr.next
            else:
                curr = curr.next
            nextCurr = nextCurr.next
            # else:
            #     curr = curr.next
        return head

        