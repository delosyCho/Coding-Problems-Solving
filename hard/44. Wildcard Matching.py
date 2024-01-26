def check_word(w1, w2):
    check = True
    for j in range(len(w1)):
        if w2[j] == '?':
            continue
        if w1[j] != w2[j]:
            check = False
    return check

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        if len(p) == 0 and len(s) == 0:
            return True
        
        if len(p) == 0 and len(s) > 0:
            return False

        if len(s) == 0:
            if len(p.replace('*', '')) == 0:
                return True
            else:
                return False

        m = len(s) + 1
        n = len(p) + 1
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for j in range(len(p)):
            count = 0
            for k in range(j, len(p)):
                if p[k] != '*':
                    count += 1

            pc = 0
            for i in range(len(s)):
                if len(s) - i - count < 0:
                    # print('!')
                    break

                if i == 0 and j == 0 and (p[j] == '?' or p[j] == s[i]):
                    dp[i][j] = 1

                if p[j] == '*':
                    

                    if i == len(s) - 1 and dp[i][j-1] == 1:
                        dp[i][j] = 1

                    if j == 0:
                        dp[i][j] = 1
                    elif dp[i][j-1] == 1 and p[j-1] == '*':
                        dp[i][j] = 1
                    elif i > 0 and dp[i-1][j-1] == 1:
                        dp[i][j] = 1
                    elif i > 0 and dp[i-1][j] == 1:
                        dp[i][j] = 1

                if j != 0:
                    if dp[i][j - 1] == 1:
                        pc = 1
                
                    if (p[j-1] == '*' and dp[i][j - 1] == 1) or (i > 0 and dp[i - 1][j - 1] == 1):
                        if p[j] == '?' or p[j] == s[i]:
                            dp[i][j] = 1
                            
                            # break
                
                        

        # print(len(dp), len(dp))
        for j in range(len(p)):
            a = []
            for i in range(len(s)):
                a.append(dp[i][j])
            # print(p[j], a)

        if dp[len(s) - 1][len(p) - 1] == 1:
            return True        
        return False
