# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    count = 0

    def preorder_traverse(self, root, maxValue) -> None:
        if root is None:
            return
        if root.val >= maxValue:
            self.count += 1
            maxValue = root.val
        self.preorder_traverse(root.left, maxValue)
        self.preorder_traverse(root.right, maxValue)

    def goodNodes(self, root: TreeNode) -> int:
        self.preorder_traverse(root, float('-inf'))
        return self.count
