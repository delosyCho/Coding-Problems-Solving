class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 0

        string = str(s)
        
        acc = 0

        result = 0

        i = 0
        e = len(s)
        for j in list(reversed(range(len(s)))):
            if s[j] == '(':
                e = j
            else:
                break

        while i < len(s):
            right = 0
            left = 0

            length = 0

            check = True
            for j in range(i, e):
                if s[j] == '(':
                    left += 1
                else:
                    right += 1

                if left < right:
                    i = j + 1
                    check = False
                    break
                if left == right:
                    length = j - i + 1
                    print(length, s[i:j+1])
            result = max(result, length) 
            print('start:', i, left, right)

            if check is True:
                left_none = 0

                if left > right and right == 0:
                    if left - right >= 2:
                        i += left - right
                    else:
                        i += 1
                else:
                    i += 1
            
        return result
                