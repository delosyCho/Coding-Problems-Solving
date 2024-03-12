class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_price = -1
        max_price = -1

        total_profit = 0
        direction = -1

        for p, price in enumerate(prices):
            if buy_price == -1:
                buy_price = price
            if max_price == -1:
                max_price = price
                continue
            
            last_price = prices[p-1]

            if price == last_price:
                continue
            elif price > last_price:
                direction = 1
            else:
                if direction == 1:
                    total_profit += (last_price - buy_price)
                    print(buy_price, last_price)
                    max_price = price
                buy_price = price

                direction = 0                
            print('check:', price, direction)
        
        if direction == 1:
            total_profit += (prices[-1] - buy_price)
        
        return total_profit

            


