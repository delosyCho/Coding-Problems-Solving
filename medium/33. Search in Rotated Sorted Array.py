class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        pivot = -1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        while start <= end:
            mid = (end + start) // 2
            if mid == 0:
                if nums[mid] > nums[mid + 1]:
                    pivot = mid
                    break
            elif mid == len(nums) - 1:
                if nums[mid] < nums[mid - 1]:
                    pivot = mid
                    break
            else:
                if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                    pivot = mid
                    break

                if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                    pivot = mid
                    break
            
            if nums[-1] > nums[mid]:
                end = mid - 1
            if nums[-1] < nums[mid]:
                start = mid + 1
            mid = (end + start) // 2
        # print(pivot)

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if mid < len(nums) - pivot - 1:
                idx = pivot + 1 + mid
            else:
                idx = mid - (len(nums) - pivot - 1)
            # print(idx, nums[idx], mid, pivot, target)
            if nums[idx] == target:
                return idx

            if nums[idx] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

