class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return [newInterval]

        for i in range(len(intervals)):
            if newInterval[0] <= intervals[i][0] <= newInterval[1]:
                intervals[i][0] = newInterval[0]
            if newInterval[0] <= intervals[i][1] <= newInterval[1]:
                intervals[i][1] = newInterval[1]

            if i == 0:
                if newInterval[1] < intervals[i][0]:
                    intervals.insert(0, newInterval)
                    break
            
            if i == len(intervals) - 1:
                if newInterval[0] > intervals[i][1]:
                    intervals.append(newInterval)
                    break
                
            if i > 0:
                # print('@@@', )
                if intervals[i - 1][1] < newInterval[0] and newInterval[1] < intervals[i][0]:
                    intervals.insert(i, newInterval)
                    break

        if len(intervals) == 1:
            if intervals[0][0] < newInterval[0]:
                intervals.append(newInterval)
            else:
                intervals.insert(0, newInterval)

        result = []
        for interval in intervals:
            if len(result) == 0:
                result.append(interval)
            else:
                if result[-1][1] >= interval[0]:
                    result[-1][1] = max(interval[1], result[-1][1])
                else:
                    result.append(interval)

        return result