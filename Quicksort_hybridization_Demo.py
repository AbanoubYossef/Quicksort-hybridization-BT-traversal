import random

def hybrid_sort(my_list, threshold=30):
    def insertion_sort(my_list, left, right):
        comparisons_counter = 0
        assignments_counter = 0

        for current_index in range(left + 1, right + 1):
            key = my_list[current_index]
            previous_index = current_index - 1

            while previous_index >= left and my_list[previous_index] > key:
                comparisons_counter += 1
                my_list[previous_index + 1] = my_list[previous_index]
                assignments_counter += 1
                previous_index -= 1

            my_list[previous_index + 1] = key
            assignments_counter += 1

        return comparisons_counter, assignments_counter

    def quicksort(my_list, left, right):
        def partition(my_list, left, right):
            pivot = my_list[left]
            storedindex = left + 1
            comparisons = 0
            assignments = 0

            for item in range(left + 1, right + 1):
                comparisons += 1
                if my_list[item] <= pivot:
                    assignments += 1
                    my_list[storedindex], my_list[item] = my_list[item], my_list[storedindex]
                    storedindex += 1

            assignments += 3
            my_list[left], my_list[storedindex - 1] = my_list[storedindex - 1], my_list[left]
            return storedindex - 1, comparisons, assignments

        stack = [(left, right)]
        comparisons = 0
        assignments = 0

        while stack:
            left, right = stack.pop()
            size = right - left + 1

            if size < threshold:
                comp, assign = insertion_sort(my_list, left, right)
                comparisons += comp
                assignments += assign
            else:
                pivot_index, comp, assign = partition(my_list, left, right)
                comparisons += comp
                assignments += assign

                if pivot_index - left < right - pivot_index:
                    stack.append((left, pivot_index - 1))
                    stack.append((pivot_index + 1, right))
                else:
                    stack.append((pivot_index + 1, right))
                    stack.append((left, pivot_index - 1))

        return comparisons, assignments

    return quicksort(my_list, 0, len(my_list) - 1)


def test_hybrid_sort():
    # Generate a random list of integers
    my_list = random.sample(range(1, 100), 20)

    # Print the original list
    print("Original List:", my_list)

    # Call the hybrid_sort function
    comparisons, assignments = hybrid_sort(my_list)

    # Print the sorted list
    print("Sorted List:", my_list)

    # Print the number of comparisons and assignments
    print("Comparisons:", comparisons)
    print("Assignments:", assignments)

# Run the test case
test_hybrid_sort()

