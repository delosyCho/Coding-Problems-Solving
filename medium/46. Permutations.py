class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []

        def backtracking(arr):
            if len(arr) == len(nums):
                result.append(nums[i] for i in arr[:])        
                return
            
            for j in range(len(nums)):
                if j not in arr:
                    arr.append(j)
                    backtracking(arr)
                    arr.pop()
        backtracking([])

        return result