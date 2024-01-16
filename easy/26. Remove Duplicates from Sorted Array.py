class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        result = []
        for i in range(0, len(nums) - 1):
            if nums[i] != nums[i + 1]:
                result.append(nums[i])
        
        if len(result) == 0:
            result.append(nums[0])

        if result[-1] != nums[-1]:
            result.append(nums[-1])
        nums[:len(result)] = result[:]
        return len(result)
        