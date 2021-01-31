'''
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
'''

from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: 'Node') -> 'Node':
    '''
        Strategy:
        Use queue and level order first
    '''

    if not root:
        return root

    q = deque()
    q.append((root, 0))

    while q:
        curr, level = q.popleft()

        if q and q[0][1] == level:
            curr.next = q[0]
        else:
            curr.next = None

        if curr.left:
            q.append((curr.left, level + 1))
        if curr.right:
            q.append((curr.right, level + 1))

    return root
