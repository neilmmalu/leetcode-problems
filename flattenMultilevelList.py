'''
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]

'''

from collections import deque


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten(head: 'Node') -> 'Node':
    if not head:
        return head

    stack = deque()
    dummyHead = Node(0, None, head, None)

    prev = dummyHead

    stack.append(head)

    while stack:
        curr = stack.pop()

        curr.prev = prev
        prev.next = curr

        if curr.next:
            stack.append(curr.next)

        if curr.child:
            stack.append(curr.child)
            curr.child = None

        prev = curr

    dummyHead.next.prev = None
    return dummyHead.next