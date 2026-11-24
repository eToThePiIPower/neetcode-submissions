class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_top = False

        # iterate over matrix and set top element of column / left element of row
        # to zero if there is a zero in it. For the first row, use variable `zero_top`
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i != 0: matrix[i][0] = 0
                    if i == 0: zero_top = True

        # set zeros
        for i in range(len(matrix) - 1, 0, -1):
            for j in range(len(matrix[0]) - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0: matrix[i][j] = 0
        if matrix[0][0] == 0:
            for i in range(len(matrix)): matrix[i][0] = 0
        if zero_top:
            for j in range(len(matrix[0])): matrix[0][j] = 0

        