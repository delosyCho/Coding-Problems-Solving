
class Solution(object):
    def __init__(self):
        self.dp = {} # key: (s1, s2), value: bool

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if (s1, s2) in self.dp:
            return self.dp[(s1, s2)]
        
        if s1 == s2:
            self.dp[(s1, s2)] = True
            return True

        if len(s1) != len(s2):
            self.dp[(s1, s2)] = False
            return False

        # Prunning
        if sorted(s1) != sorted(s2):
            # Memorization
            self.dp[(s1, s2)] = False
            return False

        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True

            if self.isScramble(s1[:i], s2[len(s2)-i:]) and self.isScramble(s1[i:], s2[:len(s2)-i]):
                return True
        self.dp[(s1, s2)] = False
        return False
        
