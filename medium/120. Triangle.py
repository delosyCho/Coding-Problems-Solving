class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        num_of_lines = len(triangle)

        dp = []
        for n in range(num_of_lines):
            line = [999999] * len(triangle[n])
            dp.append(line)
        
        dp[0][0] = triangle[0][0]

        for n in range(num_of_lines - 1):
            for j in range(len(triangle[n])):
                dp[n + 1][j] = min(dp[n][j] + triangle[n + 1][j], dp[n + 1][j])
                dp[n + 1][j + 1] = min(dp[n][j] + triangle[n + 1][j + 1], dp[n + 1][j + 1])

        return min(dp[-1])                
