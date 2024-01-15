class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def backtracking(arr, index):
            if sum(arr) >= target:
                if sum(arr) == target:
                    result.append(arr[:])
                return

            for i in range(index, len(candidates)):
                arr.append(candidates[i])
                backtracking(arr, i)
                arr.pop()

        backtracking([], 0)

        return result


