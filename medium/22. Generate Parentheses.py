class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def backtracking(arr, left, right):
            if left == n and right == n:
                result.append(''.join(arr))
                return

            if left < n:
                arr.append('(')
                backtracking(arr, left + 1, right)
                arr.pop()
            if right < n and right < left:
                arr.append(')')
                backtracking(arr, left, right + 1)
                arr.pop()

        backtracking([], 0, 0)
        return result
        