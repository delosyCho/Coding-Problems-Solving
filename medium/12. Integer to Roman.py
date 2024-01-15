class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        symbol_dict = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
            
            900: 'CM',
            400: 'CD',
            90: 'XC',
            40: 'XL',
            9: 'IX',
            4: 'IV'
        }

        value_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        value_list = [1000, 500, 100, 50, 10, 5, 1,
        900, 90, 9, 400, 40, 4]
        # symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        # for s in range(1, len(symbols)):
        #     for s2 in range(0, s - 1):
        #         new_value = value_dict[symbols[s]] - value_dict[symbols[s2]]
        #         new_symbol = symbols[s] + symbols[s2]
        #         symbol_dict[new_value] = new_symbol
        #         value_list.append(new_value)

        value_list.sort()
        value_list = list(reversed(value_list))

        result = ''
        for value in value_list:
            while num >= value:
                num -= value
                result += symbol_dict[value]
        
        return result