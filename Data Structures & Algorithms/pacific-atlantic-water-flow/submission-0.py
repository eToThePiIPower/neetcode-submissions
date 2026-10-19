from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(queue: deque, visited: set) -> None:
            while queue:
                row, col = queue.pop()
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for d_row, d_col in directions:
                    next_row, next_col = d_row + row, d_col + col
                    if (
                        0 <= next_row < rows and
                        0 <= next_col < cols and
                        (next_row, next_col) not in visited and
                        heights[next_row][next_col] >= heights[row][col]
                    ):
                        visited.add((next_row, next_col))
                        queue.append((next_row, next_col))

        rows, cols = len(heights), len(heights[0])
        pac_vis = set()
        atl_vis = set()
        pac_queue = deque()
        atl_queue = deque()

        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0:
                    pac_vis.add((row, col))
                    pac_queue.append((row, col))
                if row == rows - 1 or col == cols - 1:
                    atl_vis.add((row, col))
                    atl_queue.append((row, col))
        
        bfs(pac_queue, pac_vis)
        bfs(atl_queue, atl_vis)

        results = []
        for cell in atl_vis:
            if cell in pac_vis: results.append(cell)
        return results
