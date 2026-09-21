# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = [root]
        visible = []
        while queue:
            visible.append(queue[-1].val)
            new_queue = []
            for item in queue:
                if item.left: new_queue.append(item.left)
                if item.right: new_queue.append(item.right)
            queue = new_queue
        return visible
