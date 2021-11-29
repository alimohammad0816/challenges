class BinaryTree:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right      


def tree_tracker(tree: BinaryTree):
    for i in tree.__dict__.values():
        if isinstance(i, BinaryTree):
            tree_tracker(i)

        else:
            print(i)


tree = BinaryTree(3, BinaryTree(1, {"1", 2, 3}, 3), BinaryTree(5, BinaryTree(6, [1, 2], 8), BinaryTree(9, 10, 11)))

tree_tracker(tree)
