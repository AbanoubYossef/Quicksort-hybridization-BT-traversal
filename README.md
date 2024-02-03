# Sorting and Tree Traversal Algorithms

This repository contains Python implementations and comparative analyses of sorting algorithms (quicksort and hybrid sort) and iterative vs recursive inorder traversal of a balanced binary search tree.

## Sorting Algorithms

### Quicksort
- Implementation of the Quicksort algorithm for sorting a list of integers.
- The `quicksort` function efficiently sorts the input list using the divide-and-conquer approach.

### Hybrid Sort
- Implementation of the Hybrid Sort algorithm, combining Quicksort and Insertion Sort for optimized performance.
- The `hybrid_sort` function dynamically chooses between Quicksort and Insertion Sort based on a specified threshold.

### Testing and Analysis
- The `test_sorting_algorithm` function evaluates the performance of a sorting algorithm on a given list.
- The `run_tests` function runs multiple tests on Hybrid Quicksort with varying threshold values and visualizes the results.

## Tree Traversal

### Binary Search Tree Construction
- The `TreeNode` class and `array_to_binary_tree` function are used to create a balanced binary search tree from a sorted array.

### Inorder Traversal
- Comparative analysis of recursive and iterative inorder traversals using the `recursive_inorder_traversal` and `iterative_inorder_traversal` functions.

### Comparative Analysis
- The `comparative_analysis` function generates a range of sorted arrays, constructs balanced binary search trees, and compares recursive and iterative inorder traversal operations.

## Getting Started

1. Ensure you have Python installed on your machine.
2. Clone this repository:

```bash
git clone https://github.com/your-username/your-repository.git
```

3. Navigate to the project directory:

```bash
cd your-repository
```

4. Run the tests and comparative analysis:

```bash
python your_script_name.py
```

5. View the generated plots:

   - `QuicksortHybridizationTime.png` and `QuicksortHybridizationOperations.png` for sorting analysis.
   - `recursive_iterative_in_order_traversal.png` for tree traversal analysis.


