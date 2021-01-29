'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    s1, s2 = 0, 0

    while l1:
        s1 = s1 * 10 + l1.val
        l1 = l1.next

    while l2:
        s2 = s2 * 10 + l2.val
        l2 = l2.next

    total = s1 + s2

    head = None
    while total:
        newNode = ListNode(total % 10)
        if not head:
            head = newNode
        else:
            newNode.next = head
            head = newNode

        total //= 10

    return head if head else ListNode(0)
