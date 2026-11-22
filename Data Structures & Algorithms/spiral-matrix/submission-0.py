class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        dirs = (0, 1, 0, -1, 0) # (0, 1), (1, 0), (0, -1), (-1, 0)
        visited = [[False] * n for _ in range(m)]

        row = col = dirs_idx = 0
        result = []

        for _ in range(m * n):
            result.append(matrix[row][col])
            visited[row][col] = True

            next_row = row + dirs[dirs_idx]
            next_col = col + dirs[dirs_idx + 1]

            if (next_row < 0 or next_row >= m or
                next_col < 0 or next_col >= n or
                visited[next_row][next_col]):
                dirs_idx = (dirs_idx + 1) % 4
            
            row += dirs[dirs_idx]
            col += dirs[dirs_idx + 1]
        
        return result