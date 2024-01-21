class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        string_check =False
        pattern_check = False

        result = []

        def backtracking(i, j):
            if i >= len(s) or j >= len(p):
                check = False
                
                if j == len(p) - 2:
                    if p[-1] == '*':
                        return True
                elif j < len(p) - 2:
                    if p[j + 1] == '*':
                        check = check | backtracking(i, j + 2)
                    
                return check
            
            if i == len(s) - 1:
                if p[-1] == '*':
                    if j == len(p) - 2:
                        if s[-1] == p[-2] or p[-2] == '.':
                            return True
                elif j == len(p) - 1:
                    if p[-1] == s[-1] or p[-1] == '.':
                        return True

            my_result = False

            if j + 1 < len(p) and p[j + 1] == '*':
                while True:
                    if j + 3 >= len(p):
                        break

                    if p[j] == p[j + 2] and p[j + 3] == '*':
                        j += 2
                    else:
                        break

            if j + 1 < len(p):
                if p[j + 1] == '*':
                    if s[i] == p[j] or p[j] == '.':
                        my_result = backtracking(i + 1, j) | my_result
                    my_result = backtracking(i, j + 2) | my_result

                if s[i] == p[j] or p[j] == '.':
                    print(i + 1, j + 1)
                    my_result = backtracking(i + 1, j + 1) | my_result

            return my_result

        return backtracking(0, 0)
        return True


            
