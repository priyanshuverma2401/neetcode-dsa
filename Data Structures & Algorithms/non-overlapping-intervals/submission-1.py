class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: i[0])

        count = 0
        temp = intervals[0]
        for interval in intervals[1:]:
            if temp[1] > interval[0]:
                count += 1
                if interval[1] < temp[1]: temp = interval
            else:
                temp = interval
        return count

            
        