# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dum = ListNode(next=head)
        l , r = dum , head

        while n > 0 and r :
            n -= 1
            r = r.next

        while r:
            l = l.next
            r = r.next

        l.next = l.next.next

        return dum.next