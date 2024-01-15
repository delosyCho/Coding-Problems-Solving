class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        word = str(x)

        for i in range(len(word) // 2):
            if word[i] != word[-1-i]:
                return False
        return True
        