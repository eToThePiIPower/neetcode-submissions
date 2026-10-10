# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # hash table of indexes in inorder for fast lookup
        lookup = {val: idx for idx, val in enumerate(inorder)}

        def buildSubTree(
            preorder_start: int,
            inorder_start: int,
            size: int
        ) -> Optional[TreeNode]:
            if size <= 0: return None

            root_val = preorder[preorder_start]
            root_inorder_idx = lookup[root_val]
            left_size = root_inorder_idx - inorder_start
            right_size = size - left_size - 1

            left_child = buildSubTree(
                preorder_start + 1,
                inorder_start,
                left_size
                )
            right_child = buildSubTree(
                preorder_start + 1 + left_size,
                root_inorder_idx + 1,
                right_size
            )

            return TreeNode(root_val, left_child, right_child)


        return buildSubTree(0, 0, len(preorder))