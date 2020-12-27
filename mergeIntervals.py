# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]
# Explanation: Since intervals[1, 3] and [2, 6] overlaps, merge them into[1, 6].

# Input: intervals = [[1, 4], [4, 5]]
# Output: [[1, 5]]
# Explanation: Intervals[1, 4] and [4, 5] are considered overlapping.

from typing import List
import math


def merge(intervals: List[List[int]]) -> List[List[int]]:
    '''
        Strategy:
        Sort by first value
        In sorted intervals if idx-1 is less than existing result, merge
    '''

    intervals.sort(key=lambda x: x[0])

    result = []
    idx = 0

    while idx < len(intervals):
        if not result or intervals[idx][0] > result[-1][1]:
            result.append(intervals[idx])
        else:
            result[-1] = [min(intervals[idx][0], result[-1][0]),
                          max(intervals[idx][1], result[-1][1])]
        idx += 1
    return result


if __name__ == "__main__":
    intervals = [[12, 15], [1, 3], [0, 6], [5, 10], [15, 18]]
    print(merge(intervals))
