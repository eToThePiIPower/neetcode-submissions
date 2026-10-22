from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        cycle = False
        edges_dict = defaultdict(list)
        for v1, v2 in edges:
            edges_dict[v1].append(v2)
            edges_dict[v2].append(v1)
        
        def dfs(vertex: int) -> None:
            nonlocal cycle, visited
            if vertex in visited:
                cycle = True
                return
            visited.add(vertex)
            for v in edges_dict[vertex]:
                edges_dict[v].remove(vertex)
                dfs(v)
        
        dfs(0)

        print(f"{visited}, {cycle}")
        return not cycle and len(visited) == n

