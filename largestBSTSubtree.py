'''
Given the root of a binary tree, find the largest subtree, which is also a Binary Search Tree (BST), where the largest means subtree has the largest number of nodes.

A Binary Search Tree (BST) is a tree in which all the nodes follow the below-mentioned properties:

The left subtree values are less than the value of their parent (root) node's value.
The right subtree values are greater than the value of their parent (root) node's value.
Note: A subtree must include all of its descendants.

Follow up: Can you figure out ways to solve it with O(n) time complexity?
'''

import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def largestBSTSubtree(root: TreeNode) -> int:

    def dfs(node):
        if not node:
            return 0, math.inf, -math.inf

        # Size of l/r subtree, smallest val on l/r, biggest val on the l/r
        l_n, l_min, l_max = dfs(node.left)
        r_n, r_min, r_max = dfs(node.right)

        # Node is part of the BST
        if l_max < node.val < r_min:
            return l_n + r_n + 1, min(l_min, node.val), max(node.val, r_max)
        else:
            return max(l_n, r_n), -math.inf, math.inf

    return dfs(root)[0]
