"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start
and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval
newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still
does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
"""

class Solution:
    def insert(self, intervals: "List[int]", newInterval: 'Interval') -> 'List[Interval]':
        # init data
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        output = []
        # add all intervals starting before newInterval
        while idx < n and new_start > intervals[idx][0]:
            output.append(intervals[idx])
            idx += 1

        # add new interval
        # if there is no over lap, just add the interval
        if not output or output[-1][1] < new_start:
            output.append(newInterval)

        # if there is an over lap, merge with the last interval
        else:
            output[-1][1] = max(output[-1][1], new_end)

        # add the remaining intervals, merge with new Interval if needed.
        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx += 1
            if output[-1][1] < start:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], end)
        return output

    # both the time and space complexity are: O(N)


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4, 8]
res = Solution().insert(intervals, newInterval)
assert res == [[1,2],[3,10],[12,16]]
























