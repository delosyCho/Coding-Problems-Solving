class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        my_dict = {}

        disabled_element = {}
        
        result = []
        print(candidates)
            
        def backtracking(arr, index):
            if sum(arr) >= target:
                if sum(arr) == target:
                    my_tuple = tuple(arr[:-1])
                    if my_tuple not in my_dict:
                        result.append(arr[:])
                        my_dict[my_tuple] = ''
                
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                arr.append(candidates[i])
                backtracking(arr, i+1)
                arr.pop()

        backtracking([], 0)

        return result


        