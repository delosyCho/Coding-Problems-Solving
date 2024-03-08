class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        M = len(matrix)
        N = len(matrix[0])

        dp_r = [[0] * N for _ in range(M)]
        dp_c = [[0] * N for _ in range(M)]
        
        adj_r = [[0] * N for _ in range(M)]
        adj_c = [[0] * N for _ in range(M)]

        result = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == "1":
                    if r == 0:
                        adj_r[r][c] = 1
                    elif adj_r[r-1][c] > 0:
                        adj_r[r][c] = adj_r[r-1][c] + 1
                    else:
                        adj_r[r][c] = 1

                    if c == 0:
                        adj_c[r][c] = 1
                    elif adj_c[r][c-1] > 0:
                        adj_c[r][c] = adj_c[r][c-1] + 1
                    else:
                        adj_c[r][c] = 1

        dp_r = adj_r
        for r in range(len(matrix)):
            # print(adj_r[r])

            stack = []

            for c in range(len(matrix[r])):
                # print(stack)

                if stack == []:
                    stack.append([c, dp_r[r][c]])
                else:
                    width = c
                    height = dp_r[r][c]
                    while stack != [] and stack[-1][1] > height:
                         value = stack.pop()
                         width = value[0] 
                         size = value[1] * (c - value[0]) 
                         if result < size: 
                            result = size
                    stack.append([width, dp_r[r][c]])
            for value in stack: 
                size = value[1] * (len(matrix[r]) - value[0])
                if result < size:
                    result = size

        return result