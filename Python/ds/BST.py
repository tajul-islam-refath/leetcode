class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if key <= root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None:
            return False

        if root.key == key:
            return True

        if key <= root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=" ")
            self.inorder_traversal(root.right)


tree = BST()
tree.insert(5)
tree.insert(6)
tree.insert(1)
tree.insert(4)
tree.insert(3)
tree.insert(7)
tree.insert(20)

print(tree.search(tree.root, 20))
print(tree.search(tree.root, 0))

tree.inorder_traversal(tree.root)
