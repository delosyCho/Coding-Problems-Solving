class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        
        length = 200
        for word in strs:
            length = min(length, len(word))
        
        result = ""
        
        for j in range(length):
            character = strs[0][j]

            check = True
            for i in range(1, len(strs)):
                word = strs[i]
                if word[j] != character:
                    check = False
                    break
            
            if check is False:
                break
            result += character
        return result
            






        