"""
UNIT 5 DISCUSSION: SEARCH ALGORITHMS
Compare linear search and binary search using small and large
datasets, edge cases, and a real-world example.
"""

from time import perf_counter


def linear_search(lst, target):
    """Return the target's index, or -1 if it is not found."""

    # Linear search checks one element at a time.
    # In the worst case, it checks all n elements, making it O(n).
    for index, value in enumerate(lst):
        if value == target:
            return index

    return -1


def binary_search(lst, target):
    """Search a sorted list and return the target's index or -1."""
    left = 0
    right = len(lst) - 1

    # Each iteration eliminates about half of the remaining elements.
    # This gives binary search O(log n) worst-case time complexity.
    while left <= right:
        middle = (left + right) // 2

        if lst[middle] == target:
            return middle
        elif lst[middle] < target:
            # The target can only be to the right of the midpoint.
            left = middle + 1
        else:
            # The target can only be to the left of the midpoint.
            right = middle - 1

    return -1


def compare_searches(dataset, target):
    """Display each algorithm's result and average search time."""
    repetitions = 100

    print(f"\nDataset size: {len(dataset):,}")
    print(f"Target: {target}")

    for search in (linear_search, binary_search):
        start = perf_counter()

        for _ in range(repetitions):
            result = search(dataset, target)

        average_time = (perf_counter() - start) / repetitions

        print(
            f"{search.__name__}: index = {result}, "
            f"average time = {average_time * 1_000_000:.3f} microseconds"
        )


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")
    print("Indexes begin at 0. A result of -1 means not found.")
    print("Times are averages of 100 searches and vary between runs.")

    print("\n=== SMALL DATASET TEST ===")
    small_dataset = [10, 20, 30, 40, 50]

    # Both algorithms return 3 because 40 is at index 3.
    compare_searches(small_dataset, 40)

    # Both return -1 because 35 is not in the list.
    compare_searches(small_dataset, 35)

    print("\n=== LARGE DATASET TEST ===")
    large_dataset = list(range(100_000))

    # Both return 99,999, the last index.
    # Linear search examines all 100,000 elements.
    # Binary search examines only 17 midpoint elements for this target.
    compare_searches(large_dataset, 99_999)

    # Both return -1 because 100,000 is outside the dataset.
    compare_searches(large_dataset, 100_000)

    print("\nPerformance analysis:")
    print("Linear search has O(n) worst-case time complexity.")
    print("Binary search has O(log n) worst-case time complexity.")
    print("Both algorithms have O(1) best-case time complexity.")
    print("Binary search requires sorted data; linear search does not.")
    print("Sorting costs are excluded because these datasets are sorted.")
    print("Small timing differences can be affected by measurement noise.")
    print("For large datasets, halving the search space saves many checks.")

    print("\n=== EDGE CASE TESTS ===")

    edge_cases = [
        ("Empty list", [], 10, -1),
        ("Single element, found", [10], 10, 0),
        ("Single element, absent", [10], 20, -1),
        ("First position", [10, 20, 30], 10, 0),
        ("Last position", [10, 20, 30], 30, 2),
    ]

    # An empty list and a missing value return -1.
    # A matching single element or first element returns 0.
    # The last element in a three-element list has index 2.
    for label, dataset, target, expected in edge_cases:
        linear_result = linear_search(dataset, target)
        binary_result = binary_search(dataset, target)

        print(
            f"{label}: linear = {linear_result}, "
            f"binary = {binary_result}, expected = {expected}"
        )

    print("\n=== REAL-WORLD SEARCH SCENARIO ===")

    # A company searches a sorted list of employee IDs.
    employee_ids = [1002, 1015, 1028, 1040, 1056, 1073]
    target_id = 1040

    compare_searches(employee_ids, target_id)

    print("Both algorithms find employee ID 1040 at index 3.")
    print("Binary search suits repeated searches of a large sorted ID list.")
    print("Linear search suits small or unsorted lists.")
    print("Sorting an unsorted list for just one search may add extra work.")


if __name__ == "__main__":
    main()