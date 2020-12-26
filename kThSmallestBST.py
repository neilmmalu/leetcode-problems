# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root: TreeNode, k: int) -> int:
    '''
        Strategy:
        Naive: Inorder traversal.
        return result[k]
    '''
    result = []
    inorder(root, result)
    return result[k-1]


def inorder(root: TreeNode, result: List[int]) -> None:
    if not root:
        return

    inorder(root.left, result)
    result.append(root.val)
    inorder(root.right, result)
