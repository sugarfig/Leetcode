# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        walker = head
        counter = 0
        if head == None:
            return None
        
        while walker != None:
            counter += 1
            walker = walker.next
        print(counter)
        middle = math.ceil(counter / 2)
        print(middle)
        newWalker = head
        for i in range(1, middle):
            newWalker = newWalker.next

        if counter % 2 == 0:
            newWalker = newWalker.next

        return newWalker