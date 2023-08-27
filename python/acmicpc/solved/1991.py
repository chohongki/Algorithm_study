# 이진트리

class BinaryTree:
    def __init__(self):
        self.root = None

    def search(self, item):
        return self._search(self.root, item)

    def _search(self, node, item):
        if node is None or node.item == item:
            return node
        a = self._search(node.left, item)
        if a is None:
            return self._search(node.right, item)
        else:
            return a

    def preorder(self, node):
        if node:
            print(node.item, end='')
            if node.left:
                self.preorder(node.left)
            if node.right:
                self.preorder(node.right)

    def inorder(self, node):
        if node:
            if node.left:
                self.inorder(node.left)
            print(node.item, end='')
            if node.right:
                self.inorder(node.right)

    def postorder(self, node):
        if node:
            if node.left:
                self.postorder(node.left)
            if node.right:
                self.postorder(node.right)
            print(node.item, end='')

class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


tree = BinaryTree()
tree.root = Node('A')

N = int(input())

for _ in range(N):
    root, left, right = input().split()
    root = tree.search(root)
    root.left = None if left=='.' else Node(left)
    root.right = None if right=='.' else Node(right)

tree.preorder(tree.root)
print()
tree.inorder(tree.root)
print()
tree.postorder(tree.root)