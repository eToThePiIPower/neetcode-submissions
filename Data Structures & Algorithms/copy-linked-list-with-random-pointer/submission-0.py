"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyMap = dict()
        copyMap[None] = None

        node = head
        while node:
            copyMap[node] = Node(node.val)
            node = node.next
        
        node = head
        while node:
            copyMap[node].next = copyMap[node.next]
            copyMap[node].random = copyMap[node.random]
            node = node.next
        
        return copyMap[head]
        
