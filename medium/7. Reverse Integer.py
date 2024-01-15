class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_minus = False
        if x < 0:
            is_minus = True
            x = x * -1

        digit_point = 1

        max_digit_point = 0
        for i in range(1, 32):
            if x >= 10 ** (max_digit_point + 1):
                max_digit_point += 1
            else:
                break

        input_num = int(x)

        digit_list = []
        for i in list(reversed(range(max_digit_point + 1))):
            base = 0
            for j in range(1, 10):
                if j * 10 ** i <= input_num < (j + 1) * 10 ** i:
                    base = j

            digit_list.append(base)
            input_num -= base * 10 ** i


        result = 0
        base = 0
        for i in range(len(digit_list)):
            result += 10**base * digit_list[i]
            base += 1
        
        if result > 2**31:
            result = 0
        
        if is_minus is True:
            result = result * -1
            
        return result



        