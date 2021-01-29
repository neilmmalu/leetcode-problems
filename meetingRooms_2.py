'''
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Input: intervals = [[7,10],[2,4]]
Output: 1
'''

from typing import List


def minMeetingRooms(intervals: List[List[int]]) -> int:
    '''
        Strategy:
        Sort the start times and end times for all intervals
        Keep a count of number of rooms, and available rooms
        If the end time of a prev meeting is less than start time, make room available
        Otherwise, add another room
    '''
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])

    s, e = 0, 0
    numRooms, available = 0, 0

    while s < len(starts):
        if starts[s] < ends[e]:
            if not available:
                numRooms += 1
            else:
                available -= 1
            s += 1
        else:
            available += 1
            e += 1

    return numRooms


if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(minMeetingRooms(intervals))
