class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        num_of_path = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(0, m + 1):
            num_of_path[i][0] = 1
        for j in range(0, n + 1):
            num_of_path[0][j] = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                num_of_path[i][j] = num_of_path[i-1][j] + num_of_path[i][j-1] 

        # for p in num_of_path:
        #     print(p)

        return num_of_path[m-1][n-1]

