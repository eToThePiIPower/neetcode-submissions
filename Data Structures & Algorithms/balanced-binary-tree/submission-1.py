# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def treeHeight(node):
            if not node:
                return 0
            left_height = treeHeight(node.left)
            if left_height == -1: # unbalanced
                return -1
            right_height = treeHeight(node.right)
            if right_height == -1: #unbalanced
                return -1
            if abs(left_height - right_height) > 1: #unbalanced
                return -1
            return max(left_height, right_height) + 1
        return treeHeight(root) != -1