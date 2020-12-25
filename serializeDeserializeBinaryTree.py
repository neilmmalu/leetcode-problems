# Definition for a binary tree node.

from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        q = deque()

        result = []

        q.append((root, 0))

        while q:
            node, height = q.popleft()
            val = node.val if node else None
            if val == None:
                result.append('')
            else:
                result.append(str(val))
            if node:
                q.append((node.left, height + 1))
                q.append((node.right, height + 1))

        return ','.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        arr = data.split(',')

        q = deque()
        root = TreeNode(int(arr[0]))
        q.append(root)

        i = 1

        while q and i < len(arr):
            curr = q.popleft()
            if arr[i]:
                left = TreeNode(int(arr[i]))
                curr.left = left
                q.append(left)
            i += 1
            if arr[i]:
                right = TreeNode(int(arr[i]))
                curr.right = right
                q.append(right)
            i += 1
        return root
