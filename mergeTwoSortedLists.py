# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

# Input: l1 = [1, 2, 4], l2 = [1, 3, 4]
# Output: [1, 1, 2, 3, 4, 4]

# Input: l1 = [], l2 = [0]
# Output: [0]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    dummyHead = ListNode()
    curr = dummyHead
    while l1 and l2:
        n = None
        if l1.val < l2.val:
            n = l1
            l1 = l1.next
        else:
            n = l2
            l2 = l2.next
        n.next = None
        curr.next = n
        curr = n

    if not l1:
        curr.next = l2

    if not l2:
        curr.next = l1

    return dummyHead.next
