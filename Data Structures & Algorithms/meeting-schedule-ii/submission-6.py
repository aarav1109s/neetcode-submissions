"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        start, end = [], []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        s, e = 0, 0
        res = 0
        count = 0
        while s < len(start) and e < len(end):
            while s < len(start) and start[s] < end[e]:
                s += 1
                count += 1
                res = max(count, res)
            while e < len(end) and s < len(start) and start[s] >= end[e]:
                e += 1
                count -= 1
        
        return res

        