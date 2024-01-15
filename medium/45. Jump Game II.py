class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        length_dict = {}

        for i in range(len(nums)):
            if i not in length_dict:
                base_length = 0
            else:
                base_length = length_dict[i]
            
            for j in range(1, nums[i] + 1):
                if i + j not in length_dict:
                    length_dict[i + j] = base_length + 1
                else:
                    length_dict[i + j] = min(
                        length_dict[i + j], base_length + 1
                    )
        
        return length_dict[len(nums) - 1]


        