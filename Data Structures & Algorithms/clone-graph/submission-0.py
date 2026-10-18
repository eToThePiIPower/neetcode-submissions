"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(current_node: Optional['Node']) -> Optional['Node']:
            if current_node is None: return
            if current_node in clones: return clones[current_node]
            cloned_node = Node(current_node.val)
            clones[current_node] = cloned_node
            for neighbor in current_node.neighbors:
                cloned_node.neighbors.append(dfs(neighbor))
            return cloned_node
        
        clones = dict()
        return dfs(node)