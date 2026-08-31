# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validateBST(root, (-math.inf, math.inf))
    def validateBST(self, root: Optional[TreeNode], prev: tuple[int, int]) -> bool:
        if not root:
            return True
        if root.val <= prev[0] or root.val >= prev[1]:
            return False
        return (
            self.validateBST(root.left, (prev[0], root.val))
            and self.validateBST(root.right, (root.val, prev[1]))
        )
        