import random
import time
import matplotlib.pyplot as plt
import os 

def hybrid_sort(my_list, threshold):
    def insertion_sort(my_list, left, right):
        for current_index in range(left + 1, right + 1):
            key = my_list[current_index]
            previous_index = current_index - 1

            while previous_index >= left and my_list[previous_index] > key:
                my_list[previous_index + 1] = my_list[previous_index]
                previous_index -= 1

            my_list[previous_index + 1] = key

        return my_list

    def quicksort(my_list, left, right):
        def partition(my_list, left, right):
            pivot = my_list[left]
            storedindex = left + 1
            for item in range(left + 1, right + 1):
                if my_list[item] <= pivot:
                    my_list[storedindex], my_list[item] = my_list[item], my_list[storedindex]
            my_list[left], my_list[storedindex - 1] = my_list[storedindex - 1], my_list[left]
            return storedindex - 1

        stack = [(left, right)]
        while stack:
            left, right = stack.pop()
            size = right - left + 1
            if size < threshold:
                my_list = insertion_sort(my_list, left, right)
            else:
                pivot_index = partition(my_list, left, right)
                if pivot_index - left < right - pivot_index:
                    stack.append((left, pivot_index - 1))
                    stack.append((pivot_index + 1, right))
                else:
                    stack.append((pivot_index + 1, right))
                    stack.append((left, pivot_index - 1))
        return my_list

    return quicksort(my_list, 0, len(my_list) - 1)

def test_sorting_algorithm(algorithm, my_list):
    start_time = time.time()
    my_list= algorithm(my_list)
    end_time = time.time()
    elapsed_time = end_time - start_time

    return elapsed_time

def generate_random_list(size):
    return [random.randint(1, 1000) for _ in range(size)]

def run_tests(nr_tests=100):
    list_size = 1000
    threshold_values = list(range(1, 61))  # Vary the threshold from 1 to 60
    random_list = generate_random_list(list_size)
    output_file_path = os.path.join(os.getcwd(), 'result2.txt')

    with open(output_file_path, 'w') as output_file:
        hs_times = []

        for threshold in threshold_values:
            total_hs_time = 0
            output_file.write(f"For the threshold is {threshold}, the number of operations and the time are =>\n")

            for test_num in range(nr_tests):
                my_list_copy = random_list.copy()
                output_file.write(f"  Test {test_num + 1}:\n")

                # Add debugging prints
                print(f"  Running test {test_num + 1} with threshold {threshold}")
                try:
                    hs_time = test_sorting_algorithm(lambda lst: hybrid_sort(lst, threshold), my_list_copy)
                    output_file.write(f"    Hybrid Sort time: {hs_time}\n")
                    total_hs_time += hs_time
                except Exception as e:
                    print(f"    Test {test_num + 1} failed with error: {e}")
                    output_file.write(f"    Test {test_num + 1} failed with error: {e}\n")

            avg_hs_time = total_hs_time / nr_tests
            output_file.write(f"  Average Hybrid Sort time for threshold {threshold}: {avg_hs_time}\n")
            hs_times.append(avg_hs_time)

        # Plot the results for time
        plt.plot(threshold_values, hs_times, label='Hybrid Quicksort')
        plt.xlabel('Threshold Value')
        plt.ylabel('Average Elapsed Time (seconds)')
        plt.title('Performance of Hybrid Quicksort for Different Threshold Values (Time)')
        plt.legend()
        plt.savefig('time_plot2.png')  # Save the plot before displaying

        output_file.write("Test results saved to files: time_plot.png and operations_plot.png\n")

# Run the tests and visualize the results
run_tests()

