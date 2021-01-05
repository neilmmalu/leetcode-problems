# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Input: root = [1, null, 2, 3]
# Output: [1, 3, 2]

# Input: root = []
# Output: []

# Input: root = [1]
# Output: [1]
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode) -> List[int]:
    '''
        Strategy:
        Iterative solution required:
        Iterative DFS:
            push into stack
            if left exists, push left into stack

    '''
    if not root:
        return []

    result = []

    q = deque()
    curr = root

    while curr or q:
        while curr:
            q.append(curr)
            curr = curr.left

        curr = q.pop()
        result.append(curr.val)
        curr = curr.right

    return result


if __name__ == "__main__":
    t3 = TreeNode(3)
    t2 = TreeNode(2, t3, None)
    t1 = TreeNode(1, None, t2)
    print(inorderTraversal(t1))
