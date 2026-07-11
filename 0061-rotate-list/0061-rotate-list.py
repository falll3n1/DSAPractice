# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0 :
            return head

        count = 1
        tail = head

        while tail.next:
            count += 1
            tail = tail.next
        
        k = k % count

        if k == 0 : return head

        cur = head
        prev = None

        for _ in range(count - k):
            prev , cur = cur , cur.next

        tail.next = head
        prev.next = None

        return cur