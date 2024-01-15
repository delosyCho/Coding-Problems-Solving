class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = -1
        cur_str = []

        for i in range(len(s)):
            if s[i] in cur_str:
                max_length = max(max_length, len(cur_str))
                index = cur_str.index(s[i])
                cur_str = cur_str[index + 1:]
            cur_str.append(s[i])
        max_length = max(max_length, len(cur_str))

        return max_length


        if len(max_str) < len(cur_str):
            max_str = cur_str
        return len(max_str)


