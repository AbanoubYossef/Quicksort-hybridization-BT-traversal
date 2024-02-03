import random
import matplotlib.pyplot as plt
# Definition of a binary tree node
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Function to convert a sorted array to a balanced binary search tree
def array_to_binary_tree(arr, start, end):
    # Base case: if the start index is greater than the end index, return None
    if start > end:
        return None
    
    # Calculate the middle index of the array
    mid = (start + end) // 2
    
    # Create a new tree node with the value at the middle index
    root = TreeNode(arr[mid])
    
    # Recursively build the left subtree with elements before the middle index
    root.left = array_to_binary_tree(arr, start, mid - 1)
    
    # Recursively build the right subtree with elements after the middle index
    root.right = array_to_binary_tree(arr, mid + 1, end)
    
    # Return the root of the constructed binary search tree
    return root

# Iterative Inorder Traversal
def iterative_inorder_traversal(root):
    stack = []      # Stack to keep track of nodes
    current = root   # Start from the root
    ops = 0          # Counter to track operations

    # Loop until there are nodes in the stack or the current node is not None
    while current or stack:
        # Traverse all the way to the left, pushing nodes onto the stack
        while current:
            stack.append(current)
            current = current.left

        # Pop a node from the stack, perform an operation, and move to the right
        current = stack.pop()
        ops += 1
        current = current.right

    return ops

# Recursive Inorder Traversal
def recursive_inorder_traversal(root):
    ops = 0          # Counter to track operations

    # Base case: if the root is not None, perform inorder traversal
    if root:
        # Recursively traverse the left subtree
        ops += recursive_inorder_traversal(root.left)
        
        # Perform an operation (e.g., visit the current node)
        ops += 1

        # Recursively traverse the right subtree
        ops += recursive_inorder_traversal(root.right)

    return ops

# Function to perform comparative analysis of recursive and iterative inorder traversals
def comparative_analysis(start, end, increment):
    print("Number of Nodes\tRecursive Ops\tIterative Ops")
    nodes_list = []            # List to store the number of nodes
    recursive_ops_list = []    # List to store recursive operation counts
    iterative_ops_list = []    # List to store iterative operation counts
    
    # Loop through the range of number of nodes with the specified increment
    for num_nodes in range(start, end + 1, increment):
        # Generate a sorted array of random values to construct a binary search tree
        arr = random.sample(range(1, 100000), num_nodes)
        
        root = array_to_binary_tree(arr, 0, num_nodes - 1)
        
        # Recursive traversal
        recursive_ops = recursive_inorder_traversal(root)
        
        # Iterative traversal
        iterative_ops = iterative_inorder_traversal(root)
        
        # Store the results in lists
        nodes_list.append(num_nodes)
        recursive_ops_list.append(recursive_ops)
        iterative_ops_list.append(iterative_ops)
        
        # Print the results for the current number of nodes
        print(f"{num_nodes}\t\t\t{recursive_ops}\t\t\t{iterative_ops}")

    # Plotting the results
    plt.plot(nodes_list, recursive_ops_list, label='Recursive Ops')
    plt.plot(nodes_list, iterative_ops_list, label='Iterative Ops')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Number of Operations')
    plt.legend()
    plt.savefig('recursive_iterative_in_order_traversal.png')  # Save the plot as an image
    plt.show()

# Set your range and increment values
start_nodes = 100
end_nodes = 1000
increment = 100

# Perform the comparative analysis and plot the results
comparative_analysis(start_nodes, end_nodes, increment)
