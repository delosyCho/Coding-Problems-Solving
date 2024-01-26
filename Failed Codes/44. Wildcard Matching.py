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
        if len(s) > 0 and len(p) == 0:
            return False

        if len(s) == 0 and len(p) == 0:
            return True

        while p.find('**') != -1:
            p = str(p).replace('**', '*')
        
        if len(p) == 0:
            return True

        forward_check = True
        backward_check = True

        if p[0] == '*':
            forward_check = False
        if p[-1] == '*':
            backward_check = False

        p = p.strip('*')
        tks = p.split('*')
        
        if len(tks) == 1 and len(tks[0]) == 0:
            return True

        i, j = 0, 0
        if forward_check is True:
            if len(s) < len(tks[0]):
                return False
            
            if check_word(s[:len(tks[0])], tks[0]):
                i += len(tks[0])
                j += 1

                if j == len(tks):
                    if backward_check is False:
                        return True

                if len(tks) == 1 and i == len(s):
                    return True
            else:
                return False
        print('tks', tks, forward_check)
        def backtacking(i, j):                
            if i >= len(s) or j >= len(tks):
                return False

            if i + len(tks[j]) > len(s):
                return False

            if len(s) < 10:
                print(i, j, tks, s[i: i+len(tks[j])] == tks[j])

            while i + len(tks[j]) <= len(s):
                if check_word(s[i: i+len(tks[j])], tks[j]):
                    break
                else:
                    i += 1     

            result = False
            if check_word(s[i: i+len(tks[j])], tks[j]):
                if j == len(tks) - 1:
                    if len(s) < 10:
                        print('!!!!')
                    if i + len(tks[j]) == len(s) or backward_check is False:
                        return True
                    
                result = backtacking(i+1, j) | result
                result = backtacking(i+len(tks[j]), j+1) | result
            else:
                result = backtacking(i+1, j) | result
            return result
        return backtacking(i, j)