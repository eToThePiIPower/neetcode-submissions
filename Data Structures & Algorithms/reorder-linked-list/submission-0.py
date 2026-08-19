# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the midpoint (final value of slow)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half, ends up in prev
        prev, curr = None, slow
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # merge the lists
        l1, l2 = head, prev
        while l2.next:
            t1, t2 = l1.next, l2.next
            l1.next = l2
            l2.next = t1
            l1, l2 = t1, t2