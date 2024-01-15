class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        index0 = -1
        index1 = -1
        if (len(nums1) + len(nums2)) % 2 == 0:
            index0 = int(int(len(nums1) + len(nums2)) / 2) - 1
            index1 = int(int(len(nums1) + len(nums2)) / 2)
        else:
            index0 = int((len(nums1) + len(nums2)) / 2)

        cnt = 0
        i = 0
        j = 0

        nums1.append(999999999)
        nums2.append(999999999)

        arr = []
        # print(index0, index1)
        while True:
            if i >= len(nums1) - 1 and j >= len(nums2):
                break

            # print(i, nums1[i], ',', j, nums2[j], cnt)

            if nums1[i] < nums2[j]:
                if cnt == index0 or cnt == index1:
                    arr.append(nums1[i])
                i += 1
            else:
                if cnt == index0 or cnt == index1:
                    arr.append(nums2[j])
                j += 1
            cnt += 1

        result = arr[0]
        if len(arr) > 1:
            result = float(arr[0] + arr[1]) / 2

        return result