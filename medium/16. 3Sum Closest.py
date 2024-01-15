class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        value = 99999999

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sum_value = nums[i] + nums[j] + nums[k]
                # print(sum_value)
                if sum_value < target:
                    j += 1
                else:
                    k -= 1
                if abs(sum_value - target) <= abs(value - target):
                    value = sum_value

        return value



        