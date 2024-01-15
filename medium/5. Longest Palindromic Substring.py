class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        p_sub = str(s[0])

        for i in range(0, len(s)):
            st = i
            en = i

            while True:
                if st - 1 < 0:
                    break
                if s[st - 1] == s[i]:
                    st -= 1
                else:
                    break

            while True:
                if en + 1 >= len(s):
                    break
                if s[en + 1] == s[i]:
                    en += 1
                else:
                    break
            # print(i, st, en)
            while True:
                if st - 1 < 0:
                    break
                if en + 1 >= len(s):
                    break
                if s[st - 1] == s[en + 1]:
                    st -= 1
                    en += 1
                else:
                    break

            if len(p_sub) < en - st + 1:
                p_sub = str(s[st:en+1])

        return p_sub
