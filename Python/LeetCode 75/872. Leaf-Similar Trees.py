# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder_traverse(self, head: TreeNode, array: list[int]):
        if head is None:
            return array
        if head.left is None and head.right is None:
            array.append(head.val)
            return array
        self.inorder_traverse(head.left, array)
        self.inorder_traverse(head.right, array)
        return array

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.inorder_traverse(root1, []) == self.inorder_traverse(root2, [])
