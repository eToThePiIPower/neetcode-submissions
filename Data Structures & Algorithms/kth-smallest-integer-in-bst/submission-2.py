# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        stack = []
        current = root
        while current or stack:
            # reach the leftmost node
            while current:
                stack.append(current)
                current = current.left

            # process the current noc
            current = stack.pop()
            count += 1
            if count == k:
                return current.val

            # queue the right node for the next iteration
            current = current.right

            