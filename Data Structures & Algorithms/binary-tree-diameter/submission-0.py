# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        def height(root: Optional[TreeNode]) -> int:
            nonlocal maxDiameter
            if root is None:
                return 0
            lHeight = height(root.left)
            rHeight = height(root.right)
            maxDiameter = max(maxDiameter, lHeight + rHeight)
            return 1 + max(lHeight, rHeight)
        height(root)
        return maxDiameter