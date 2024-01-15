class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()

        result = []
        result_dict = {}

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                mid = j + 1
                end = len(nums) - 1

                while mid < end:
                    # print(mid, end)
                    total = nums[i] + nums[j] + nums[mid] + nums[end]
                    if total == target:
                        if (nums[i], nums[j], nums[mid], nums[end]) not in result_dict:
                            result_dict[(nums[i], nums[j], nums[mid], nums[end])] = ''
                            result.append([nums[i], nums[j], nums[mid], nums[end]])
                        mid += 1
                    elif total > target:
                        end -= 1
                    else:
                        mid += 1

        return result

