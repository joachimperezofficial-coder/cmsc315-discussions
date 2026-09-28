"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS
BUBBLE SORT VS. MERGE SORT
===========================================================

This program demonstrates and compares two sorting algorithms:

1. Bubble Sort
2. Merge Sort

Two different datasets are sorted using both algorithms.
The program also tests several edge cases and explains the
differences in efficiency between Bubble Sort and Merge Sort.
"""


def bubble_sort(lst):
    """
    Sort a list using the Bubble Sort algorithm.

    A copy of the original list is created so that the
    original data is not modified.
    """

    # Create a copy of the original list.
    sorted_list = lst.copy()

    # Repeat passes through the list.
    for i in range(len(sorted_list) - 1):
        swapped = False

        # Compare each pair of adjacent elements.
        # The largest remaining value moves toward the end
        # of the list after each pass.
        for j in range(len(sorted_list) - 1 - i):

            # Swap the values if they are in the wrong order.
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = (
                    sorted_list[j + 1],
                    sorted_list[j]
                )

                swapped = True

        # If no swaps occurred during a complete pass,
        # the list is already sorted and we can stop early.
        if not swapped:
            break

    return sorted_list


def merge_sort(lst):
    """
    Sort a list using the recursive Merge Sort algorithm.

    Merge Sort divides the list into smaller halves,
    recursively sorts those halves, and then merges them
    back together in sorted order.
    """

    # Base case:
    # A list containing zero or one element is already sorted.
    if len(lst) <= 1:
        return lst.copy()

    # Find the middle position of the list.
    middle = len(lst) // 2

    # Divide the list into two halves.
    left_half = lst[:middle]
    right_half = lst[middle:]

    # Recursively sort both halves.
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merge the sorted halves together.
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    Merge two already-sorted lists into one sorted list.
    """

    result = []

    # Keep track of the current position in each list.
    left_index = 0
    right_index = 0

    # Compare values from both lists until one list is exhausted.
    while left_index < len(left) and right_index < len(right):

        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1

        else:
            result.append(right[right_index])
            right_index += 1

    # Add any remaining values from the left list.
    result.extend(left[left_index:])

    # Add any remaining values from the right list.
    result.extend(right[right_index:])

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # =====================================================
    # DATASET #1
    # =====================================================

    # Dataset #1 contains at least seven unsorted values.
    dataset1 = [42, 15, 8, 23, 4, 16, 31, 9]

    print("\n=== DATASET #1 ===")
    print("Original List:", dataset1)

    # Sort the same dataset using both algorithms.
    bubble_result1 = bubble_sort(dataset1)
    merge_result1 = merge_sort(dataset1)

    print("Bubble Sort:", bubble_result1)
    print("Merge Sort: ", merge_result1)

    # Verify that both algorithms produced the same result.
    if bubble_result1 == merge_result1:
        print("Comparison: Both algorithms produced the same sorted list.")
    else:
        print("Comparison: The algorithms produced different results.")

    # =====================================================
    # DATASET #2
    # =====================================================

    # Dataset #2 uses different values from Dataset #1.
    dataset2 = [73, 12, 95, 28, 54, 6, 41, 67, 19]

    print("\n=== DATASET #2 ===")
    print("Original List:", dataset2)

    # Sort Dataset #2 using both algorithms.
    bubble_result2 = bubble_sort(dataset2)
    merge_result2 = merge_sort(dataset2)

    print("Bubble Sort:", bubble_result2)
    print("Merge Sort: ", merge_result2)

    # Compare the sorting results.
    if bubble_result2 == merge_result2:
        print("Comparison: Both algorithms produced the same sorted list.")
    else:
        print("Comparison: The algorithms produced different results.")

    # =====================================================
    # EDGE CASE TESTS
    # =====================================================

    print("\n=== EDGE CASE TESTS ===")

    # -----------------------------------------------------
    # Edge Case #1: Empty List
    # -----------------------------------------------------

    empty_list = []

    print("\nEdge Case #1: Empty List")
    print("Original List:", empty_list)
    print("Bubble Sort:", bubble_sort(empty_list))
    print("Merge Sort: ", merge_sort(empty_list))

    print(
        "Explanation: An empty list contains no values to compare, "
        "so it is already considered sorted."
    )

    # -----------------------------------------------------
    # Edge Case #2: Already Sorted List
    # -----------------------------------------------------

    already_sorted = [1, 2, 3, 4, 5, 6, 7]

    print("\nEdge Case #2: Already Sorted List")
    print("Original List:", already_sorted)
    print("Bubble Sort:", bubble_sort(already_sorted))
    print("Merge Sort: ", merge_sort(already_sorted))

    print(
        "Explanation: Both algorithms return the same ordered list. "
        "The optimized Bubble Sort detects that no swaps are required "
        "and stops early."
    )

    # -----------------------------------------------------
    # Edge Case #3: Duplicate Values
    # -----------------------------------------------------

    duplicate_values = [5, 2, 8, 2, 5, 1, 8]

    print("\nEdge Case #3: Duplicate Values")
    print("Original List:", duplicate_values)
    print("Bubble Sort:", bubble_sort(duplicate_values))
    print("Merge Sort: ", merge_sort(duplicate_values))

    print(
        "Explanation: Both algorithms correctly sort the list while "
        "keeping all duplicate values."
    )

    # =====================================================
    # ALGORITHM COMPARISON
    # =====================================================

    print("\n=== ALGORITHM COMPARISON ===")

    print(
        "Bubble Sort repeatedly compares adjacent elements and swaps "
        "them when they are out of order."
    )

    print(
        "Bubble Sort has an average and worst-case time complexity "
        "of O(n^2). With the early-stop optimization used in this "
        "program, its best-case time complexity is O(n) when the "
        "list is already sorted."
    )

    print(
        "Merge Sort uses a divide-and-conquer strategy. It repeatedly "
        "divides the list into smaller halves, sorts those halves "
        "recursively, and merges them back together."
    )

    print(
        "Merge Sort has a time complexity of O(n log n), making it "
        "generally more efficient than Bubble Sort as the size of "
        "the dataset increases."
    )

    print(
        "However, Merge Sort requires additional memory to create "
        "and merge smaller lists, while Bubble Sort is conceptually "
        "simpler."
    )


if __name__ == "__main__":
    main()