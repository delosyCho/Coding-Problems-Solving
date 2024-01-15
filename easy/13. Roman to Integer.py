class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        my_dict = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1,

            'CM': 900,
            'XC': 90,
            'IX': 9,

            'CD': 400,
            'XL': 40,
            'IV': 4,
        }
        result = 0

        i = 0
        while i < len(s):
            if i + 1 < len(s):
                word = str(s[i:i+2])
                if word in my_dict:
                    result += my_dict[word]
                    i += 2
                    continue
            
            word = str(s[i])
            result += my_dict[word]
            i += 1

        return result
