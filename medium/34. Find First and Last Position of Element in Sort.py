class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1

        pivot = -1
        while start <= end:
            mid = (start + end) // 2
            # print(mid)
            if nums[mid] == target:
                pivot = mid
                break

            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        print(pivot)
        i = pivot
        start = i

        while True:
            i -= 1

            if i < 0:
                break
            
            if nums[i] == target:
                start = i
            else:
                break

        i = pivot
        end = i
        while True:
            i += 1

            if i >= len(nums):
                break
            
            if nums[i] == target:
                end = i
            else:
                break
        
        return [start, end]


