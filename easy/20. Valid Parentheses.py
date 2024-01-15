class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            
            if s[i] == ')' or s[i] == ']' or s[i] == '}':
                if len(stack) == 0:
                    return False
                last_char = stack.pop()
                if (last_char == '(' and s[i] != ')') \
                or (last_char == '[' and s[i] != ']') \
                or (last_char == '{' and s[i] != '}'):
                    return False
        if len(stack) > 0:
            return False
        return True

            




        