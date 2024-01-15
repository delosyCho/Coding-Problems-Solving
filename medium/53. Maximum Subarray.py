class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = -999999
        max_subarray = -999999

        for i in range(len(nums)):
            max_sum = max(max_sum + nums[i], nums[i])
            max_subarray = max(max_subarray, max_sum)
            # print(i, max_sum)
        return max_subarray

