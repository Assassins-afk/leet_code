class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        valid_intervals = 0
        max_end = -1

        for start, end in intervals:
            if end > max_end:

                valid_intervals += 1
                max_end = end

        return valid_intervals