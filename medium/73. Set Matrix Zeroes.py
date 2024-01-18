class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_to_zero = []
        col_to_zero = []

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    if r not in row_to_zero:
                        row_to_zero.append(r)
                    if c not in col_to_zero:
                        col_to_zero.append(c)
        
        for r in row_to_zero:
            for c in range(len(matrix[0])):
                matrix[r][c] = 0
        for r in range(len(matrix)):
            for c in col_to_zero:
                matrix[r][c] = 0
                