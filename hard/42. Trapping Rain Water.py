class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        total = 0

        left, right = 0, len(height) - 1
        left_max = height[0]
        right_max = height[-1]

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            if left_max <= right_max:
                left += 1
                if height[left] < left_max:
                    total += left_max - height[left]
            else:
                right -= 1
                if height[right] < right_max:
                    total += right_max - height[right]
                
        return total
        



        