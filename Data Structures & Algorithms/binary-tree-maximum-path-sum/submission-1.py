# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = -inf
        def dfsSum(node):
            nonlocal maxPath
            if not node: return 0
            left = dfsSum(node.left)
            right = dfsSum(node.right)
            maxPath = max(maxPath, node.val, node.val + left, node.val + right, node.val + left + right)
            return max(0, node.val, node.val + left, node.val + right)
        dfsSum(root)
        return maxPath