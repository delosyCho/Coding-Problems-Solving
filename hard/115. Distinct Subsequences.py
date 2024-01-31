class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n = len(s)
        m = len(t)
        dp = [0] * m
        
        for i in range(n):
            for j in list(reversed(range(m))):
                if s[i] == t[j]:
                    if j == 0:
                        dp[j] += 1
                    else:
                        dp[j] += dp[j - 1]
            # print(dp)
        return dp[-1] 