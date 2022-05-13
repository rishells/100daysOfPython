class Node:
    def __init__(self, value):  # Constructor
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

my_tree = BinarySearchTree()

print(my_tree.root)
