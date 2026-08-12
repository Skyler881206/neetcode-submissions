class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        remove_count = 0
        prev_end = intervals[0][1]

        for interval in intervals[1:]:
            if interval[0] >= prev_end:
                prev_end = interval[1]

            else:
                remove_count += 1
                prev_end = min(prev_end, interval[1])

        return remove_count 