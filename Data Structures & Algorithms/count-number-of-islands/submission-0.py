class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def dfs(x, y, add=0):
            nonlocal count
            if x < 0 or y < 0: return
            if x >= len(grid) or y >= len(grid[0]): return
            if grid[x][y] == "0": return
            count += add
            grid[x][y] = "0"
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                dfs(x, y, 1)
        return count

        