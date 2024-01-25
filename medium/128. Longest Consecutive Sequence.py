class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        if len(nums) == 0:
            return 0

        max_value = 1
        for n in range(len(nums)):
            if (nums[n] in dict) is False:
                dict[nums[n]] = 1
            else:
                continue

            new_value = 1
            if (nums[n] + 1 in dict) is True and (nums[n] - 1 in dict) is True:
                value_left = dict[nums[n] - 1]
                value_right = dict[nums[n] + 1]

                new_value = value_left + value_right + 1

                dict[nums[n]] = new_value
                dict[nums[n] - value_left] = new_value
                dict[nums[n] + value_right] = new_value
            elif (nums[n] + 1 in dict) is True:
                value_right = dict[nums[n] + 1]
                new_value = value_right + 1

                dict[nums[n]] = new_value
                dict[nums[n] + value_right] = new_value
            elif (nums[n] - 1 in dict) is True:
                value_left = dict[nums[n] - 1]
                new_value = value_left + 1

                dict[nums[n]] = new_value
                dict[nums[n] - value_left] = new_value
            if new_value > max_value:
                max_value = new_value
        return max_value