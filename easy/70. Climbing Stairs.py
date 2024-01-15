from collections import deque

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
    
        dict_list = {}        
        dict_list[1] = 1
        dict_list[2] = 2

        for j in range(3, n + 1):
            dict_list[j] = dict_list[j - 1] + dict_list[j - 2]

        return dict_list[n]


