class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert a node
    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    # Search a node
    def search(self, value):
        if self.root is None:
            return False

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.data == value:
                return True

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return False

    # Inorder Traversal
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    # Preorder Traversal
    def preorder(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # Postorder Traversal
    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    # Level Order Traversal
    def level_order(self):
        if self.root is None:
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            print(current.data, end=" ")

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)


# Main program
bt = BinaryTree()

bt.insert(25)
bt.insert(15)
bt.insert(40)
bt.insert(10)
bt.insert(20)
bt.insert(30)
bt.insert(50)

print("Inorder:")
bt.inorder(bt.root)

print("\nPreorder:")
bt.preorder(bt.root)

print("\nPostorder:")
bt.postorder(bt.root)

print("\nLevel Order:")
bt.level_order()

print("\n\nSearching for 30:")

if bt.search(30):
    print("30 found")
else:
    print("30 not found")
