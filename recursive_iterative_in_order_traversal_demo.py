##########################################################
# Name: Abanoub Youssef
# seria B grup 6
#Fundmental Algorthims
# assignment 8
###########################################################

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def iterative_in_order_traversal(root):
    current = root
    stack = []

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.key, end=" ")  # Perform the operation (e.g., print)
        current = current.right

def recursive_in_order_traversal(root):
    if root:
        recursive_in_order_traversal(root.left)
        print(root.key, end=" ")  # Perform the operation (e.g., print)
        recursive_in_order_traversal(root.right)

# Example Usage:
# Construct a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Iterative In-order Traversal:")
iterative_in_order_traversal(root)
print("\nRecursive In-order Traversal:")
recursive_in_order_traversal(root)