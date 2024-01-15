class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result_array = [0] * 2000
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                value = int(num1[i]) * int(num2[j])
                value = str(value)[::-1]

                for k in range(len(value)):
                    idx = i + j + k
                    result_array[idx] += int(value[k])
        print(result_array[:10])
        for i in range(2000 - 1):
            if result_array[i] >= 10:
                add = result_array[i] // 10
                result_array[i] -= add * 10
                result_array[i + 1] += add
            # result = str(result_array[i]) + result
        print(result_array[:10])

        digit_length = 0
        for i in list(reversed(range(2000))):
            if result_array[i] != 0:
                digit_length = i
                break

        result = ''
        for i in range(digit_length + 1):
            result = str(result_array[i]) + result
        return result


