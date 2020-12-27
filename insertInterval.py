# Given a set of non-overlapping intervals, insert a new interval into the intervals(merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Input: intervals = [[1, 3], [6, 9]], newInterval = [2, 5]
# Output: [[1, 5], [6, 9]]

# Input: intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval = [4, 8]
# Output: [[1, 2], [3, 10], [12, 16]]
# Explanation: Because the new interval[4, 8] overlaps with [3, 5], [6, 7], [8, 10].

# Input: intervals = [], newInterval = [5, 7]
# Output: [[5, 7]]

# Input: intervals = [[1, 5]], newInterval = [2, 3]
# Output: [[1, 5]]

from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    '''
        Strategy:
        Greedy:
        add all before newinterval
        add new interval and merge with prev if necessary
        add all after newinterval and merge if necessary
    '''
    if not intervals:
        return [newInterval]

    result = []

    idx = 0
    while idx < len(intervals) and intervals[idx][0] < newInterval[0]:
        result.append(intervals[idx])
        idx += 1

    if not result or result[-1][1] < newInterval[0]:
        result.append(newInterval)
    else:
        result[-1][1] = max(result[-1][-1], newInterval[1])

    while idx < len(intervals):
        interval = intervals[idx]
        idx += 1

        if result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])

    return result


if __name__ == "__main__":
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print(insert(intervals, newInterval))
