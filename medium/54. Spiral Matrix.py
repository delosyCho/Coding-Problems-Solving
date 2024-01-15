class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = [int(matrix[0][0])]
        matrix[0][0] = 999

        width = len(matrix[0]) - 1
        height = len(matrix) - 1

        if width == 0 and height == 0:
            return result

        i, j = 0, 0
        direction = 0
        while True:
            if direction == 0:
                while True:
                    if j == width:
                        break

                    j += 1
                    
                    result.append(int(matrix[i][j]))
                    matrix[i][j] = 999
                    if j == width:
                        break
                    if matrix[i][j + 1] == 999:
                        break
                direction += 1
            elif direction == 1:
                while True:
                    if i == height:
                        break

                    i += 1
                    
                    result.append(int(matrix[i][j]))
                    matrix[i][j] = 999
                    if i == height:
                        break
                    if matrix[i + 1][j] == 999:
                        break
                direction += 1
            elif direction == 2:
                while True:
                    if j == 0:
                        break

                    j -= 1
                    
                    result.append(int(matrix[i][j]))
                    matrix[i][j] = 999
                    if j == 0:
                        break
                    if matrix[i][j - 1] == 999:
                        break
                direction += 1
            elif direction == 3:
                while True:
                    if i == 0:
                        break
                        
                    i -= 1
                    
                    result.append(int(matrix[i][j]))
                    matrix[i][j] = 999
                    if i == 0:
                        break
                    if matrix[i - 1][j] == 999:
                        break
                direction += 1

            if direction == 4:
                direction = 0

            if direction == 0:
                if j == width:
                    break
                if matrix[i][j + 1] == 999:
                    break
            elif direction == 1:
                if i == height:
                    break
                if matrix[i + 1][j] == 999:
                    break
            elif direction == 2:
                if j == 0:
                    break
                if matrix[i][j - 1] == 999:
                    break
            elif direction == 3:
                if i == 0:
                    break
                if matrix[i - 1][j] == 999:
                    break
        return result   





