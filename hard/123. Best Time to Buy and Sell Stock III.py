class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp_left = [0] * len(prices)
        dp_right = [0] * len(prices)
        dp = [0] * len(prices)
        min_value = -1
        max_profit = -1

        for p, price in enumerate(prices):
            if min_value == -1 or min_value > price:
                min_value = price
            
            profit = price - min_value
            max_profit = max(profit, max_profit)
            dp_left[p] = max_profit
            
        max_value = -1
        max_profit = -1

        for p in list(reversed(range(1, len(prices)))):
            price = prices[p]

            if max_value == -1 or max_value < price:
                max_value = price
            
            profit = max_value - price
            max_profit = max(profit, max_profit)
            dp_right[p-1] = max_profit
        
        for p in range(len(prices)):
            dp[p] = dp_left[p] + dp_right[p]
        print(dp_left)
        print(dp_right)
        return max(dp)

