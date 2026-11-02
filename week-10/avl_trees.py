# WEEK 10 - AVL TREE

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


# Get height of a node
def height(node):
    if node is None:
        return 0
    return node.height


# Get balance factor
def get_balance(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)


# Right Rotation
def right_rotate(y):
    x = y.left
    temp = x.right

    x.right = y
    y.left = temp

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x


# Left Rotation
def left_rotate(x):
    y = x.right
    temp = y.left

    y.left = x
    x.right = temp

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


# Insert a node
def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)

    elif key > root.key:
        root.right = insert(root.right, key)

    else:
        print("Duplicate value not allowed!")
        return root

    # Update height
    root.height = 1 + max(height(root.left), height(root.right))

    # Calculate balance factor
    balance = get_balance(root)

    # LL Case
    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    # RR Case
    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    # LR Case
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # RL Case
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


# Find minimum value node
def min_value_node(root):
    current = root

    while current.left is not None:
        current = current.left

    return current


# Delete a node
def delete(root, key):
    if root is None:
        print("Value not found!")
        return root

    if key < root.key:
        root.left = delete(root.left, key)

    elif key > root.key:
        root.right = delete(root.right, key)

    else:
        # Node with no child
        if root.left is None and root.right is None:
            return None

        # Node with only right child
        elif root.left is None:
            return root.right

        # Node with only left child
        elif root.right is None:
            return root.left

        # Node with two children
        else:
            temp = min_value_node(root.right)
            root.key = temp.key
            root.right = delete(root.right, temp.key)

    # Update height
    root.height = 1 + max(height(root.left), height(root.right))

    # Calculate balance factor
    balance = get_balance(root)

    # LL Case
    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)

    # LR Case
    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # RR Case
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)

    # RL Case
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


# Search for a value
def search(root, key):
    if root is None:
        return False

    if root.key == key:
        return True

    if key < root.key:
        return search(root.left, key)

    return search(root.right, key)


# Inorder Traversal
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


# Preorder Traversal
def preorder(root):
    if root is not None:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder Traversal
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ")


# Main Program
root = None

while True:
    print("\n----- AVL TREE MENU -----")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to insert: "))
        root = insert(root, value)
        print("Value inserted successfully.")

    elif choice == 2:
        value = int(input("Enter value to delete: "))
        root = delete(root, value)
        print("Deletion operation completed.")

    elif choice == 3:
        value = int(input("Enter value to search: "))

        if search(root, value):
            print("Value found in AVL Tree.")
        else:
            print("Value not found in AVL Tree.")

    elif choice == 4:
        print("Inorder Traversal:")
        inorder(root)
        print()

    elif choice == 5:
        print("Preorder Traversal:")
        preorder(root)
        print()

    elif choice == 6:
        print("Postorder Traversal:")
        postorder(root)
        print()

    elif choice == 7:
        print("Program terminated.")
        break

    else:
        print("Invalid choice!")
