class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) <= 1:
            return intervals

        intervals.sort(key = lambda x: x[0])

        result = []
        # Keep the first interval.
        result.append(intervals[0])

        for interval in intervals[1:]:
            # If overlap is found.
            if result[-1][1] >= interval[0] and result[-1][0] <= interval[1]:
                old = result.pop()
                new = [min(old[0], interval[0]), max(old[1], interval[1])]
                result.append(new)
            else:
                result.append(interval)

        return result