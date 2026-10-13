class BinaryTree:
    def __init__(self, size):
        self.tree = [None] * size
        self.size = size

    # Insert a node
    def insert(self, value):
        for i in range(self.size):
            if self.tree[i] is None:
                self.tree[i] = value
                return
        print("Tree is full")

    # Search a node
    def search(self, value):
        for i in range(self.size):
            if self.tree[i] == value:
                return i
        return -1

    # Inorder Traversal
    def inorder(self, i=0):
        if i >= self.size or self.tree[i] is None:
            return

        self.inorder(2 * i + 1)
        print(self.tree[i], end=" ")
        self.inorder(2 * i + 2)

    # Preorder Traversal
    def preorder(self, i=0):
        if i >= self.size or self.tree[i] is None:
            return

        print(self.tree[i], end=" ")
        self.preorder(2 * i + 1)
        self.preorder(2 * i + 2)

    # Postorder Traversal
    def postorder(self, i=0):
        if i >= self.size or self.tree[i] is None:
            return

        self.postorder(2 * i + 1)
        self.postorder(2 * i + 2)
        print(self.tree[i], end=" ")

    # Display array
    def display(self):
        print(self.tree)


# Main program
bt = BinaryTree(10)

bt.insert(25)
bt.insert(15)
bt.insert(40)
bt.insert(10)
bt.insert(20)
bt.insert(30)
bt.insert(50)

print("Array representation:")
bt.display()

print("\nInorder:")
bt.inorder()

print("\nPreorder:")
bt.preorder()

print("\nPostorder:")
bt.postorder()

print("\n\nSearching for 30:")

position = bt.search(30)

if position != -1:
    print("30 found at index", position)
else:
    print("30 not found")
