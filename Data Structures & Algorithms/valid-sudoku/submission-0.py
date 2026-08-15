class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for _ in range(9)]
        colSets = [set() for _ in range(9)]
        squSets = [set() for _ in range(9)]
        for row_idx, row in enumerate(board):
            for col_idx, item in enumerate(row):
                if item == ".":
                    continue
                if item in rowSets[row_idx]:
                    return False
                if item in colSets[col_idx]:
                    return False
                if item in squSets[self.__squindex(row_idx, col_idx)]:
                    return False
                rowSets[row_idx].add(item)
                colSets[col_idx].add(item)
                squSets[self.__squindex(row_idx, col_idx)].add(item)
        return True
    
    def __squindex(self, row: int, col: int) -> int:
        return (row//3) * 3 + (col//3)