class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = 0

        min_value = 9999999
        max_value = 0

        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 99999
            
        for i in range(len(nums)):
            v = abs(nums[i]) - 1
            if v < len(nums):
                nums[v] = abs(nums[v]) * -1 
        
        missing = 1
        for i in range(len(nums)):
            if nums[i] < 0:
                missing += 1
            else:
                break
        # print(nums)
        return missing

