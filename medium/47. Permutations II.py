class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = []
        result_dict = {}

        def backtracking(arr):
            if len(arr) == len(nums):
                my_tuple = tuple(nums[i] for i in arr[:])
                # print(my_tuple)
                if my_tuple not in result_dict:
                    result_dict[my_tuple] = ''
                    result.append(nums[i] for i in arr[:])        
                return
            
            for j in range(len(nums)):
                if j not in arr:
                    arr.append(j)
                    backtracking(arr)
                    arr.pop()
        backtracking([])

        return result