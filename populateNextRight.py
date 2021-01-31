'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
'''


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: 'Node') -> 'Node':
    '''
        Strategy:
        Go down till second to last level.
        For each node, connect left to right and right to left of next if next exists
        Can also do this with queue, level order traversal and math, because it's a complete tree
    '''
    Q = root
    while root and root.left:
        n = root.left
        while root:
            root.left.next = root.right
            root.right.next = root.next and root.next.left
            root = root.next
        root = n
    return Q
