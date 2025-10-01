# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # first way i did:
    # walk thru linked list and get amount in linked list
    # then divide by 2 to get middle
    # start again from top and go to middle
    # if amount in linked list was even then go to next bc this algorithm will take the first middle one.
    # 2nd way to do:
    # have 2 pointers start at 1st linked list head then increase one by 2 and then increase the other by 1 everytime
    # do this while walker and walker.next are not null

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # walker = head
        # counter = 0
        # if head == None:
        #     return None
        
        # while walker != None:
        #     counter += 1
        #     walker = walker.next
        # # print(counter)
        # middle = math.ceil(counter / 2)
        # # print(middle)
        # newWalker = head
        # for i in range(1, middle):
        #     newWalker = newWalker.next

        # if counter % 2 == 0:
        #     newWalker = newWalker.next

        # return newWalker

        walker = head
        middle = head
        while walker != None and walker.next != None:
            middle = middle.next
            walker = walker.next.next
        return middle