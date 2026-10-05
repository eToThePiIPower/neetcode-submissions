class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        found = False
        visited = set()

        def backtrack(row, col, idx):
            nonlocal found
            if idx == len(word):
                found = True
                return
            if (row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                (row, col) in visited or
                board[row][col] != word[idx]):
                return
            
            visited.add((row, col))
            
            backtrack(row + 1, col, idx + 1)
            backtrack(row - 1, col, idx + 1)
            backtrack(row, col + 1, idx + 1)
            backtrack(row, col - 1, idx + 1)
            
            visited.remove((row, col))

        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, 0)
        return found



