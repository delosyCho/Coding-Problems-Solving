class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        index = 0
        num = min(nums)

        while True:
            count = 0

            for i in range(index, len(nums)):
                index = i
                if nums[i] == num:
                    count += 1
                    if count > 2:
                        nums[i] = -99999
                else:
                    break
            num = nums[index]

            if index == len(nums) - 1:
                break

        pointer = -1

        for i in range(len(nums)):
            if nums[i] == -99999:
                if pointer <= i:
                    pointer = i + 1

                for j in range(pointer, len(nums)):
                    if nums[j] != -99999:
                        nums[i] = nums[j]
                        nums[j] = -99999
                        pointer = j + 1
                        break
        
        length = 0
        for i in range(len(nums)):
            if nums[i] != -99999:
                length = i
            else:
                length += 1
                break
        if nums[-1] != -99999:
            length += 1
        
        print(length, nums)


        return length

            



        