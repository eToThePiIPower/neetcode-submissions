class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows_to_zero = [False] * len(matrix)
        cols_to_zero = [False] * len(matrix[0]
        )
        # iterate over matrix and set top element of column / left element of row
        # to zero if there is a zero in it. For the first row, use variable `zero_top`
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows_to_zero[i] = True
                    cols_to_zero[j] = True

        # set zeros
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if rows_to_zero[i] or cols_to_zero[j]: matrix[i][j] = 0
        