class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        visited = {}
        result = []

        def backtracking(arr):
            if len(arr) == k:
                result.append(arr[:])
                return

            start = 0
            if len(arr) > 0:
                start = arr[-1]

            for j in range(start + 1, n + 1):
                arr.append(j)
                backtracking(arr)
                arr.pop()
        backtracking([])

        return result