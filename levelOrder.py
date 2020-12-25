# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree[3, 9, 20, null, null, 15, 7],

# [
#     [3],
#     [9, 20],
#     [15, 7]
# ]
from typing import List
from queue import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: TreeNode) -> List[List[int]]:
    '''
        Strategy:
        BFS: Add tuple of (val, height to queue)
    '''

    if not root:
        return []

    q = deque()
    q.append((root, 0))

    result = []

    while q:
        node, height = q.popleft()
        if node:
            val = node.val
            if len(result) == height:
                result.append([val])
            else:
                result[height].append(val)
            q.append((node.left, height + 1))
            q.append((node.right, height + 1))

    return result


if __name__ == "__main__":
    input = [3, 9, 20, None, None, 15, 7]
    t1 = TreeNode(15)
    t2 = TreeNode(7)
    t3 = TreeNode(20, t1, t2)
    t4 = TreeNode(9)
    t5 = TreeNode(3, t4, t3)

    print(levelOrder(t5))
