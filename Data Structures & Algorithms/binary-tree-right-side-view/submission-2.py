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
            vis, new_queue = None, []
            for item in queue:
                if not vis: vis = item.val
                if item.right: new_queue.append(item.right)
                if item.left: new_queue.append(item.left)
            queue = new_queue
            visible.append(vis)
        return visible
