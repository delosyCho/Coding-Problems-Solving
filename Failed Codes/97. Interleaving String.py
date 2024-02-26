class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
        def backtracking(idx1, idx2, idx3):
            if idx3 == len(s3):
                
                if idx1 == len(s1) and idx2 == len(s2):
                    return True
                else:
                    return False

            check = False

            jump = 0
            while True:
                if len(s1) <= idx1 + jump or len(s3) <= idx3 + jump:
                    break

                if s1[idx1 + jump] == s3[idx3 + jump]:
                    jump += 1
                else:
                    break

            if jump > 0:
                check = backtracking(idx1 + jump, idx2, idx3 + jump) | check

            jump = 0
            while True:
                if len(s2) <= idx2 + jump or len(s3) <= idx3 + jump:
                    break

                if s2[idx2 + jump] == s3[idx3 + jump]:
                    jump += 1
                else:
                    break

            if jump > 0:
                check = backtracking(idx1, idx2 + jump, idx3 + jump) | check

            return check
        
        return backtracking(0, 0, 0)








