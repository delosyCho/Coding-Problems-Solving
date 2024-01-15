class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min_steps = {}
        min_steps[0] = 0

        max_available = 0

        if len(nums) <= 1:
            return True

        for i in range(len(nums)):
            if i == len(nums) - 1:
                return True

            if nums[i] != 0:
                max_available = max(i + nums[i], max_available)
            else:
                if max_available < i+1:
                    return False
        return True                
