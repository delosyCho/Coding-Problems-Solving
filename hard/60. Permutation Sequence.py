def factorial(num):
    res = 1
    for k in range(1, num + 1):
        res = res * k
    return res

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = list(range(1, n + 1))
        
        permutations = []

        k = k-1
        # total_permutations = factorial(n)
        # k = k % total_permutations

        result = []

        for i in reversed(list(range(1, n))):
            total_permutations = factorial(i)
            
            number = k // total_permutations
            result.append(nums.pop(number))
            k = k % total_permutations
        result.append(nums.pop())
        
        return ''.join(map(str, result))