# Invert a binary tree.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return

    invertTree(root.left)
    invertTree(root.right)

    left = root.left
    right = root.right
    root.right = left
    root.left = right

    return root
