# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Follow up: Could you do this in one pass?

# Input: head = [1, 2, 3, 4, 5], n = 2
# Output: [1, 2, 3, 5]

# Input: head = [1], n = 1
# Output: []

# Input: head = [1, 2], n = 1
# Output: [1]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    if not head or n < 1:
        return head

    fast, slow = head, head

    while n and fast:
        fast = fast.next
        n -= 1

    if n:
        return head

    if not n and not fast:
        return head.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return head
