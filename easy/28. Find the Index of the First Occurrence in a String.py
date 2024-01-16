class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            check = True
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    check = False
                    break
            
            if check is True:
                return i
        return -1