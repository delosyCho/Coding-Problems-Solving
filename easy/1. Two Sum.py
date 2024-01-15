class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_original = list(nums)

        def quick_sort(arr):
            if len(arr) <= 1:
                return arr
            
            pivot = arr[len(arr) // 2]  # 중간 값을 기준으로선택
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            
            return quick_sort(left) + middle + quick_sort(right)
        
        nums = quick_sort(nums)

        mid_point = len(nums) // 2
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    idx1 = -1
                    idx2 = -1

                    for k in range(len(nums_original)):
                        if nums_original[k] == nums[i] and idx1 == -1:
                            idx1 = k
                            continue
                        if nums_original[k] == nums[j] and idx2 == -1:
                            idx2 = k

                    return [idx1, idx2]
                
                if nums[i] + nums[j] > target:
                    break
        
        return False


