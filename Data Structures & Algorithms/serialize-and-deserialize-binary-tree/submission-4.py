# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ""
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("N")
        while res and res[-1] == 'N':
            res.pop()
        res = [str(i) for i in res]
        return ", ".join(res)
            
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None
        vals = data.split(", ")
        vals = deque(vals)
        root = TreeNode(vals.popleft())
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if vals:
                left = vals.popleft()
                if left != 'N':
                    node.left = TreeNode(int(left))
                    queue.append(node.left)
            if vals:
                right = vals.popleft()
                if right != 'N':
                    node.right = TreeNode(int(right))
                    queue.append(node.right)
        return root

