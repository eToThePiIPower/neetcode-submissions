# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        result = []
        current_level = 0

        while queue:
            numItems = len(queue)
            result.append([])

            for _ in range(numItems):
                current = queue.pop(0)
                result[current_level].append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            current_level += 1
        return result

