# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Given 1 -> 2 -> 3 -> 4, reorder it to 1 -> 4 -> 2 -> 3.

# Given 1 -> 2 -> 3 -> 4 -> 5, reorder it to 1 -> 5 -> 2 -> 4 -> 3.

from reverseList import reverseList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head: ListNode) -> None:
    '''
        Strategy:
        Split the list in half
        Reverse the second half
        Interleave the second half inside first half
    '''

    if not head or not head.next or not head.next.next:
        return

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    secondHalf = slow.next
    slow.next = None

    secondHalfReversed = reverseList(secondHalf)

    curr = head

    while curr and secondHalfReversed:
        temp1 = curr.next
        temp2 = secondHalfReversed.next
        curr.next = secondHalfReversed
        secondHalfReversed.next = temp1
        curr = temp1
        secondHalfReversed = temp2
