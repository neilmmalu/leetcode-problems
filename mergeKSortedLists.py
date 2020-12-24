# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
# Output: [1, 1, 2, 3, 4, 4, 5, 6]
# Explanation: The linked-lists are:
# [
#     1 -> 4 -> 5,
#     1 -> 3 -> 4,
#     2 -> 6
# ]
# merging them into one sorted list:
# 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
from typing import List
from mergeTwoSortedLists import mergeTwoLists


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[ListNode]) -> ListNode:
    '''
        Strategy:
        Merge two lists at a time
        Keep doing that until only 1 list is left
        Use merge2sortedlists
    '''
    if not lists:
        return lists

    interval = 1
    while interval < len(lists):
        idx = 0
        while idx < len(lists):
            lists[idx] = mergeTwoLists(lists[idx], lists[idx+interval])
            idx += interval*2
        interval *= 2

    return lists[0] if len(lists) > 0 else None
