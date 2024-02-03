import random
import time
import matplotlib.pyplot as plt
import os 

# Define the hybrid_sort function that performs hybrid sorting using quicksort and insertion_sort
def hybrid_sort(my_list, threshold):
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

# Define a function to run tests for hybrid quicksort with varying threshold values
def run_tests(nr_tests=100):
    # Set the size of the list to be sorted
    list_size = 10000
    # Vary the threshold from 1 to 60
    threshold_values = list(range(1, 61))
    # Generate a random list for testing
    random_list = generate_random_list(list_size)
    # Specify the output file path
    output_file_path = os.getcwd() + '/result.txt'

    with open(output_file_path, 'w') as output_file:
        hs_times = []  # List to store hybrid quicksort average times
        hs_operations = []  # List to store hybrid quicksort average operations

        # Print header for the table
        output_file.write("Threshold | Avg Time (seconds) | Avg Operations\n")
        output_file.write("-" * 45 + "\n")

        for threshold in threshold_values:
            total_hs_time = 0
            total_hs_comparisons = 0
            total_hs_assignments = 0

            for test_num in range(nr_tests):
                # Make a copy of the random list for each test
                my_list_copy = random_list.copy()
                # Test hybrid quicksort and record comparisons, assignments, and time
                hs_comparisons, hs_assignments, hs_time = test_sorting_algorithm(lambda lst: hybrid_sort(lst, threshold), my_list_copy)

                total_hs_comparisons += hs_comparisons
                total_hs_assignments += hs_assignments
                total_hs_time += hs_time

            # Calculate average time and operations for the current threshold
            avg_hs_time = total_hs_time / nr_tests
            avg_hs_operations = total_hs_comparisons + total_hs_assignments

            # Print values for each threshold in a tabular format
            output_file.write(f"{threshold:<10} | {avg_hs_time:<18.6f} | {avg_hs_operations:<15}\n")

            # Append results to respective lists
            hs_times.append(avg_hs_time)
            hs_operations.append(avg_hs_operations)

        # Plot the results for time
        plt.figure(figsize=(10, 6))
        plt.plot(threshold_values, hs_times, label='Hybrid Quicksort')
        plt.xlabel('Threshold Value')
        plt.ylabel('Average Elapsed Time (seconds)')
        plt.title('Performance of Hybrid Quicksort for Different Threshold Values (Time)')
        plt.legend()
        plt.savefig('time_plot.png')

        # Plot the results for operations
        plt.figure(figsize=(10, 6))
        plt.plot(threshold_values, hs_operations, label='Hybrid Quicksort')
        plt.xlabel('Threshold Value')
        plt.ylabel('Average Number of Operations')
        plt.title('Performance of Hybrid Quicksort for Different Threshold Values (Operations)')
        plt.legend()
        plt.savefig('operations_plot.png')

        # Show the plots
        plt.show()
        # Provide a message in the output file indicating where the result files are saved
        output_file.write("\nTest results saved to files: time_plot.png and operations_plot.png\n")

# Run the tests and visualize the results
run_tests()
