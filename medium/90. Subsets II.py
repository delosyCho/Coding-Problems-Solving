class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        count_dict = {}

        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        
        keys = count_dict.keys()
        results = []

        def backtracking(keys, idx, arr):
            if idx == len(keys):
                results.append(arr[:])
                return
        
            backtracking(keys, idx + 1, arr)
            for i in range(count_dict[keys[idx]]):
                a = [keys[idx]] * (i + 1)
                arr.extend(a)
                backtracking(keys, idx + 1, arr)
                for _ in range(i + 1):
                   arr.pop(-1) 


        backtracking(keys=keys, idx=0, arr=[])

        return results