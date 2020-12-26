# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given
# preorder = [3, 9, 20, 15, 7]
# inorder = [9, 3, 15, 20, 7]

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    '''
        Strategy:
        preStart: index of preorder: this is used to create the root
        pivot: find corresponding index in inorder
        everything on left is left subtree, right is right subtree
        left subtree is easy: preStart + 1
        right subtree: preStart + pivot - inStart + 1
    '''
    return build(0, 0, len(inorder), preorder, inorder)


def build(preStart: int, inStart: int, inEnd: int, preorder: List[int], inorder: List[int]) -> TreeNode:
    if inStart > inEnd or preStart >= len(preorder):
        return None

    pivot = inStart
    while inorder[pivot] != preorder[preStart]:
        pivot += 1

    root = TreeNode(inorder[pivot])
    root.left = build(preStart + 1, inStart, pivot - 1, preorder, inorder)
    root.right = build(preStart + pivot - inStart + 1,
                       pivot + 1, inEnd, preorder, inorder)
    return root


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    buildTree(preorder, inorder)
