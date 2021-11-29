class BinaryTree:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right      


def tree_tracker(tree: BinaryTree):
    my_tree = tree

    while my_tree:
        if any((isinstance(value, BinaryTree) for value in my_tree.__dict__.values())):
            for i in my_tree.__dict__.values():
                if isinstance(i, BinaryTree):
                    print(i)
                    my_tree = i

                else:
                    print(i)

        else:
            for i in my_tree.__dict__.values():
                print(i)
            break


tree = BinaryTree(3, 4, BinaryTree(5, BinaryTree(6, 7, 8), BinaryTree(9, 10, 11)))

tree_tracker(tree)
