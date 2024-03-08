class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        sorted_indices = sorted(range(len(ratings)), key=lambda i: ratings[i])


        dp = [-1] * len(ratings)

        for ix in sorted_indices:
            left = 9999999
            if ix > 0:
                left = ratings[ix - 1]
            
            right = 99999999
            if ix + 1 < len(ratings):
                right = ratings[ix + 1]

            thres = ratings[ix]
            if thres > left and thres > right:
                dp[ix] = max(dp[ix-1], dp[ix+1]) + 1
            elif thres > left:
                dp[ix] = dp[ix-1] + 1
            elif thres > right:
                dp[ix] = dp[ix+1] + 1
            else:
                dp[ix] = 1

        return sum(dp)
