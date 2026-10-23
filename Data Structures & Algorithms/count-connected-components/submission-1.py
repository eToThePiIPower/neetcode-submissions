class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)] # lowest node in group
        components = n

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> int:
            nonlocal components
            parent_x = find(x)
            parent_y = find(y)
            if parent_x == parent_y: return
            parent[parent_x] = parent[parent_y]
            components -= 1

        for v1, v2 in edges:
            union(v1, v2)
        return components
