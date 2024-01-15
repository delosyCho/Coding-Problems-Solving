class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums_set = list(set(nums))
        if len(nums_set) <= 1:
            return

        if len(nums) <= 1:
            return

        start = 0
        end = len(nums) - 1
        
        while nums[start] == 0:
            start += 1
            if start >= len(nums):
                break
        print('start:', start)
        while nums[end] == 2:
            end -= 1
            if end < 0:
                break

        if start >= len(nums) and end < 0:
            return 

        if end < 0:
            end = len(nums) - 1

        i = start
        if min(nums_set) != 0:
            start = 0
            i = 0

        print(start, end, i)     
        while i <= end and start < len(nums) and i < len(nums):
            print(i, nums, start, end)
            if nums[i] == 0:
                if i == start:
                    i += 1
                    start += 1
                    continue

                temp = nums[start]
                nums[start] = 0
                nums[i] = temp

                start += 1
                if i < start:
                    i += 1

            if i >= len(nums):
                break

            if nums[i] == 2:
                temp = nums[end]
                nums[end] = 2
                nums[i] = temp

                end -= 1

            if nums[i] == 1:
                i += 1
                
        print(start, end)
