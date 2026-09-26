"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: return True

        intervals.sort(key = lambda i: i.start)



        temp = intervals[0]

        for interval in intervals[1:]:
            if interval.start < temp.end: return False
            else:
                temp = interval
        return True
