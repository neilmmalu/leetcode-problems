# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(s: TreeNode, t: TreeNode) -> bool:
    if not s or not t:
        return False
    return isIdentical(s, t) or isSubtree(s.left, t) or isIdentical(s.right, t)


def isIdentical(s: TreeNode, t: TreeNode) -> bool:
    if not s and not t:
        return True

    if not s or not t:
        return False

    return s.val == t.val and isIdentical(s.left, t.left) and isIdentical(s.right, t.right)
