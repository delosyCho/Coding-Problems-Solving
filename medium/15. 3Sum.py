class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        max_value = nums[-1]
        min_value = nums[0]
        result = []
        check_dict = {}

        j = len(nums) - 1

        for i in range(len(nums) - 2):
            j = len(nums) - 1
            mid = i + 1
            while mid < j:
                total = nums[i] + nums[j] + nums[mid]
                if total <= 0:
                    if total == 0:
                        if (nums[i], nums[j]) not in check_dict:
                            check_dict[
                                (nums[i], nums[j])
                            ] = ''
                            result.append([nums[i], nums[mid], nums[j]])
                    mid += 1
                else:
                    j -= 1 

        return result