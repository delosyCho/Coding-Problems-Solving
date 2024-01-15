class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n == 0:
            return 1

        result = 1
        mul = x

        if n < 0:
            n = abs(n)
            mul = 1/x

        while True:
            if n == 0:
                return result
            
            if n % 2 == 0:
                mul = mul * mul
                n = n / 2


            n -= 1
            result = result * mul
            print(result, mul, n)
        
        .