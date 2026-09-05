class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low_n, high_n = 0, len(matrix) - 1
        n = high_n // 2
        while low_n < high_n:
            if target < matrix[n][0]:
                high_n = n - 1
                n = (high_n + low_n) // 2
            elif target > matrix[n][-1]:
                low_n = n + 1
                n = (high_n + low_n) // 2
            else:
                break
        low_m, high_m = 0, len(matrix[n]) - 1
        m = high_m // 2
        while low_m < high_m:
            if target < matrix[n][m]:
                high_m = m - 1
                m = (high_m + low_m) // 2
            elif target > matrix[n][m]:
                low_m = m + 1
                m = (high_m + low_m) // 2
            else:
                break
        return matrix[n][m] == target