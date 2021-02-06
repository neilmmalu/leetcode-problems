'''
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (x, y), its left and right children will be at positions (x - 1, y - 1) and (x + 1, y - 1) respectively.

The vertical order traversal of a binary tree is a list of non-empty reports for each unique x-coordinate from left to right. Each report is a list of all nodes at a given x-coordinate. The report should be primarily sorted by y-coordinate from highest y-coordinate to lowest. If any two nodes have the same y-coordinate in the report, the node with the smaller value should appear earlier.

Return the vertical order traversal of the binary tree.

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
'''

from typing import List
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verticalTraversal(root: TreeNode) -> List[List[int]]:
    cols = defaultdict(list)
    queue = [(root, 0)]
    while queue:
        newQueue = []
        d = defaultdict(list)
        for node, col in queue:
            d[col].append(node.val)
            if node.left:
                newQueue += (node.left, col-1),
            if node.right:
                newQueue += (node.right, col+1),
        for i in d:
            cols[i].extend(sorted(d[i]))
        queue = newQueue
    return [cols[i] for i in sorted(cols)]
