class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        step = 0

        start = 0
        end = len(height) - 1

        max_container = 0
        
        while start < end:
            area = min(height[start], height[end]) * (end - start) 
            max_container = max(max_container, area)

            is_changed = False
            if height[start] < height[end]:
                j = start + 1
                while j < end:
                    if height[j] > height[start]:
                        start = j
                        is_changed = True
                        break
                    j += 1
            else:
                j = end - 1
                while start < j:
                    if height[j] > height[end]:
                        end = j
                        is_changed = True
                        break
                    j -= 1

            if is_changed is False:
                if height[start] > height[end]:
                    j = start + 1
                    while j < end:
                        if height[j] > height[start]:
                            start = j
                            is_changed = True
                            break
                        j += 1
                else:
                    j = end - 1
                    while start < j:
                        if height[j] > height[end]:
                            end = j
                            is_changed = True
                            break
                        j -= 1

            if is_changed is False:
                break
            
        return max_container 
