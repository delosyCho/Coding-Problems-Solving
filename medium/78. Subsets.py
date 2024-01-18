class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def backtracking(arr, index):
            if index == len(nums):
                result.append(arr[:])
                return
            arr.append(nums[index])
            backtracking(arr, index + 1)
            arr.pop()

            backtracking(arr, index + 1)

        backtracking([], 0)

        return result
        