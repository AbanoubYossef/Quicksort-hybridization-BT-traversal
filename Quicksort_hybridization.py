import random
import time
import matplotlib.pyplot as plt

# Define the quicksort function that takes a list as input
def quicksort(my_list):
    # Define the partition function that helps in the quicksort process
    def partition(my_list, left, right):
        # Choose the leftmost element as the pivot
        pivot = my_list[left]
        # Initialize the storedindex to the element next to the pivot
        storedindex = left + 1
        # Initialize counters for comparisons and assignments
        comparisons = 0
        assignments = 0

        # Iterate through elements from left+1 to right
        for item in range(left + 1, right + 1):
            comparisons += 1
            # Compare each element with the pivot
            if my_list[item] <= pivot:
                assignments += 1
                # Swap elements if they are less than or equal to the pivot
                my_list[storedindex], my_list[item] = my_list[item], my_list[storedindex]
                storedindex += 1

        # Finalize the position of the pivot in the sorted list
        assignments += 3
        my_list[left], my_list[storedindex - 1] = my_list[storedindex - 1], my_list[left]
        # Return the index where the pivot is placed, comparisons, and assignments
        return storedindex - 1, comparisons, assignments

    # Initialize a stack with the range of indices to be sorted
    stack = [(0, len(my_list) - 1)]

    # Initialize counters for comparisons and assignments
    comparisons = 0
    assignments = 0

    # Iterate until the stack is empty
    while stack:
        # Pop the left and right indices from the stack
        left, right = stack.pop()
        # Check if there are elements to be sorted
        if left < right:
            # Perform partitioning and get pivot index, comparisons, and assignments
            pivot_index, comp, assign = partition(my_list, left, right)
            comparisons += comp
            assignments += assign

            # Decide which subarray to sort first based on the pivot's position
            if pivot_index - left < right - pivot_index:
                stack.append((left, pivot_index - 1))
                stack.append((pivot_index + 1, right))
            else:
                stack.append((pivot_index + 1, right))
                stack.append((left, pivot_index - 1))

    # Return the total comparisons and assignments performed during the sorting
    return comparisons, assignments


# Define the hybrid_sort function that performs hybrid sorting using quicksort and insertion_sort
def hybrid_sort(my_list, threshold=30):
    # Define the insertion_sort function for small subarrays
    def insertion_sort(my_list, left, right):
        comparisons_counter = 0
        assignments_counter = 0

        # Iterate through the elements in the subarray
        for current_index in range(left + 1, right + 1):
            key = my_list[current_index]
            previous_index = current_index - 1

            # Compare and swap elements until the correct position is found
            while previous_index >= left and my_list[previous_index] > key:
                comparisons_counter += 1
                my_list[previous_index + 1] = my_list[previous_index]
                assignments_counter += 1
                previous_index -= 1

            # Place the key in its correct position
            my_list[previous_index + 1] = key
            assignments_counter += 1

        # Return the total comparisons and assignments
        return comparisons_counter, assignments_counter

    # Define the quicksort function for larger subarrays
    def quicksort(my_list, left, right):
        # Define the partition function for quicksort
        def partition(my_list, left, right):
            pivot = my_list[left]
            storedindex = left + 1
            comparisons = 0
            assignments = 0

            # Iterate through elements and partition around the pivot
            for item in range(left + 1, right + 1):
                comparisons += 1
                if my_list[item] <= pivot:
                    assignments += 1
                    my_list[storedindex], my_list[item] = my_list[item], my_list[storedindex]
                    storedindex += 1

            # Finalize the position of the pivot in the sorted list
            assignments += 3
            my_list[left], my_list[storedindex - 1] = my_list[storedindex - 1], my_list[left]
            return storedindex - 1, comparisons, assignments

        # Initialize the stack with the initial subarray
        stack = [(left, right)]
        comparisons = 0
        assignments = 0

        # Iterate until the stack is empty
        while stack:
            # Pop the left and right indices from the stack
            left, right = stack.pop()
            size = right - left + 1

            # Use insertion_sort for small subarrays
            if size < threshold:
                comp, assign = insertion_sort(my_list, left, right)
                comparisons += comp
                assignments += assign
            else:
                # Use quicksort for larger subarrays
                pivot_index, comp, assign = partition(my_list, left, right)
                comparisons += comp
                assignments += assign

                # Decide which subarray to sort first based on the pivot's position
                if pivot_index - left < right - pivot_index:
                    stack.append((left, pivot_index - 1))
                    stack.append((pivot_index + 1, right))
                else:
                    stack.append((pivot_index + 1, right))
                    stack.append((left, pivot_index - 1))

        # Return the total comparisons and assignments performed during the sorting
        return comparisons, assignments

    # Call quicksort with the entire input list and return the result
    return quicksort(my_list, 0, len(my_list) - 1)


# Define a function to test a sorting algorithm on a given list
def test_sorting_algorithm(algorithm, my_list):
    # Record the start time
    start_time = time.time()
    # Run the sorting algorithm and get comparisons, assignments, and elapsed time
    comparisons, assignments = algorithm(my_list)
    # Record the end time
    end_time = time.time()
    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Return comparisons, assignments, and elapsed time
    return comparisons, assignments, elapsed_time

# Define a function to generate a random list of a given size
def generate_random_list(size):
    # Generate a list of random integers between 1 and 1000
    return [random.randint(1, 1000) for _ in range(size)]

# Define a function to run tests for regular and hybrid quicksort
def run_tests(nr_tests=100):
    # Generate a list of sizes ranging from 100 to 10000
    list_sizes = [100 * i for i in range(1, 101)]  
    qs_times = []  # List to store regular quicksort times
    hs_times = []  # List to store hybrid quicksort times
    qs_operations = []  # List to store regular quicksort operations
    hs_operations = []  # List to store hybrid quicksort operations

    # Iterate through different list sizes
    for size in list_sizes:
        # Test regular quicksort and record comparisons, assignments, and time
        qs_comparisons, qs_assignments, qs_time = test_sorting_algorithm(quicksort, generate_random_list(size))
        # Test hybrid quicksort and record comparisons, assignments, and time
        hs_comparisons, hs_assignments, hs_time = test_sorting_algorithm(hybrid_sort, generate_random_list(size))

        # Append results to respective lists
        qs_times.append(qs_time)
        hs_times.append(hs_time)
        qs_operations.append(qs_comparisons + qs_assignments)
        hs_operations.append(hs_comparisons + hs_assignments)

    # Plot the results for time
    plt.figure(figsize=(10, 6))
    plt.plot(list_sizes, qs_times, label='Regular Quicksort')
    plt.plot(list_sizes, hs_times, label='Hybrid Quicksort')
    plt.xlabel('Number of Nodes in Binary Tree')
    plt.ylabel('Elapsed Time (seconds)')
    plt.title('Comparison of Regular and Hybrid Quicksort (Time)')
    plt.legend()
    plt.savefig('QuicksortHybridizationTime.png')

    # Plot the results for operations
    plt.figure(figsize=(10, 6))
    plt.plot(list_sizes, qs_operations, label='Regular Quicksort')
    plt.plot(list_sizes, hs_operations, label='Hybrid Quicksort')
    plt.xlabel('Number of Nodes in Binary Tree')
    plt.ylabel('Number of Operations')
    plt.title('Comparison of Regular and Hybrid Quicksort (Operations)')
    plt.legend()
    plt.savefig('QuicksortHybridizationOperations.png')

    # Show the plots
    plt.show()

# Run the tests and visualize the results
run_tests()


