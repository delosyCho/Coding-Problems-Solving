class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        if dividend < 0:
            dividend = abs(dividend)
            sign = -1 * sign
        
        if divisor < 0:
            divisor = abs(divisor)
            sign = -1 * sign
        

        total_count = 0
        while dividend >= divisor:
            count = 1
            acc_divisor = divisor
            while True:
                if acc_divisor + acc_divisor < dividend:
                    acc_divisor = acc_divisor + acc_divisor
                    count = count + count
                else:
                    # print(acc_divisor, count)
                    break

            dividend -= acc_divisor
            total_count += count
        
        if total_count * sign > 2**31 - 1:
            return 2**31 - 1
        if total_count * sign < -2**31:
            return -2**31
        
        return total_count * sign
 
        