class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        m = len(board)
        n = len(board[0])

        result = []

        matrix = board

        def backtracking(arr, x, y, index):
            for i in [x - 1, x + 1]:
                j = y
                if i < 0 or i >= m:
                    continue
                    
                if (i, j) in arr:
                    continue

                if matrix[i][j] == word[index]:
                    if index == len(word) - 1:
                        result.append(0)
                        return
                    
                    arr.append((i, j))
                    backtracking(arr, i, j, index + 1)
                    arr.pop()

            for j in [y - 1, y + 1]:
                i = x
                if j < 0 or j >= n:
                    continue

                if (i, j) in arr:
                    continue

                if matrix[i][j] == word[index]:
                    if index == len(word) - 1:
                        result.append(0)
                        return
                    
                    arr.append((i, j))
                    backtracking(arr, i, j, index + 1)
                    arr.pop()
                    
                

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    backtracking([(i, j)], i, j, 1)

                if len(result) > 0:
                    return True
        
        return False




        