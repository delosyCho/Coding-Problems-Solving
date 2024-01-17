class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        start = 0
        end = len(matrix) * len(matrix[0]) - 1
        
        while start <= end:
            mid = (start + end) // 2
            i = mid // len(matrix[0])
            j = mid % len(matrix[0])

            if matrix[i][j] == target:
                return True
            # print(mid, i, j, matrix[i][j], target)
            if matrix[i][j] > target:
                end = mid - 1
            else:
                start = mid + 1

        return False

