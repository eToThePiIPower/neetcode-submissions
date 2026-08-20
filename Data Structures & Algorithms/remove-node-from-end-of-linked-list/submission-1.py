# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        before = ListNode(None, head)
        slow, fast = before, head

        # move fast to separate by n
        for _ in range(n):
            fast = fast.next
        
        # move flow and fast until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next
        
        # slow.next is the node to be skipped
        slow.next = slow.next.next

        
        return before.next