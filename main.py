class AVLNode:
    # Constructor for the AVLNode class, initializing an AVL tree node.
    def __init__(self, key):
        self.key = key  # Key of the node
        self.height = 1  # Height of the node (initial height is 1 since the new node is a leaf)
        self.left = None  # Left child of the node
        self.right = None  # Right child of the node

    # Method to represent the tree as a string for easy visualization.
    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.key) + "\n"  # Form the string for the current node
        if self.left:  # If there is a left child
            ret += self.left.__str__(level + 1, "L--- ")  # Recursively add the left child
        if self.right:  # If there is a right child
            ret += self.right.__str__(level + 1, "R--- ")  # Recursively add the right child
        return ret  # Return the string

# Function to get the height of a node
def get_height(node):
    if not node:  # If the node is None
        return 0
    return node.height  # Return the height of the node

# Function to get the balance of a node (difference in heights of the left and right subtrees)
def get_balance(node):
    if not node:  # If the node is None
        return 0
    return get_height(node.left) - get_height(node.right)  # Return the balance of the node

# Function to perform a left rotation around node z
def left_rotate(z):
    y = z.right  # y is the right child of z
    T2 = y.left  # T2 is the left subtree of y

    y.left = z  # z becomes the left child of y
    z.right = T2  # T2 becomes the right child of z

    # Update the heights of nodes z and y
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y  # Return the new root of the subtree

# Function to perform a right rotation around node y
def right_rotate(y):
    x = y.left  # x is the left child of y
    T3 = x.right  # T3 is the right subtree of x

    x.right = y  # y becomes the right child of x
    y.left = T3  # T3 becomes the left child of y

    # Update the heights of nodes y and x
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x  # Return the new root of the subtree

# Function to find the node with the minimum value in the tree
def min_value_node(node):
    current = node  # Start from the given node
    while current.left is not None:  # Traverse to the leftmost child
        current = current.left
    return current  # Return the node with the minimum value

# Function to insert a new key into the AVL tree
def insert(root, key):
    if not root:  # If the tree is empty, create a new node
        return AVLNode(key)

    if key < root.key:  # If the key is less than the root, insert in the left subtree
        root.left = insert(root.left, key)
    elif key > root.key:  # If the key is greater than the root, insert in the right subtree
        root.right = insert(root.right, key)
    else:  # If the key already exists in the tree, do not insert it again
        return root

    # Update the height of the current node
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # Get the balance factor of the current node
    balance = get_balance(root)

    # If the node becomes unbalanced, perform one of the 4 possible rotations

    # Left Left Case
    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:  # Left Right Case
            root.left = left_rotate(root.left)
            return right_rotate(root)

    # Right Right Case
    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:  # Right Left Case
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root  # Return the root of the tree
