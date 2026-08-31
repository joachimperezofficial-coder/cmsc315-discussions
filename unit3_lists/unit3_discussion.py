"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    Inserts a value into the list at the specified index.
    """

    # insert() places the new value at the given position.
    # If the value is inserted near the beginning or middle,
    # the elements after it have to shift to the right.
    # Inserting at the end usually requires less shifting.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    Removes and returns the value at the specified index.
    Returns None when the index is invalid.
    """

    # Check the index before deleting so the program does not
    # crash by trying to remove an item that does not exist.
    if index < 0 or index >= len(lst):
        return None

    # pop() removes the item and returns the removed value.
    # Items after the deleted value shift to the left.
    return lst.pop(index)


def search_value(lst, value):
    """
    Searches for a value in the list.
    Returns the index when found or -1 when not found.
    """

    # This is a linear search because the list is checked
    # one item at a time from beginning to end.
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    # The entire list was searched without finding the value.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # INSERTION TESTS
    # ===============================

    print("\n=== INSERTION TESTS ===")

    numbers = [10, 20, 30, 40]

    print("Original list:", numbers)

    # Insert at the beginning.
    insert_at(numbers, 0, 5)
    print("After inserting 5 at the beginning:", numbers)

    # Insert near the middle.
    middle_index = len(numbers) // 2
    insert_at(numbers, middle_index, 25)
    print("After inserting 25 in the middle:", numbers)

    # Insert at the end.
    insert_at(numbers, len(numbers), 50)
    print("After inserting 50 at the end:", numbers)

    # ===============================
    # DELETION TESTS
    # ===============================

    print("\n=== DELETION TESTS ===")

    print("Starting list:", numbers)

    # Delete the first item.
    removed = delete_at(numbers, 0)
    print("Removed from beginning:", removed)
    print("Updated list:", numbers)

    # Delete an item from the middle.
    middle_index = len(numbers) // 2
    removed = delete_at(numbers, middle_index)
    print("Removed from middle:", removed)
    print("Updated list:", numbers)

    # Delete the final item.
    removed = delete_at(numbers, len(numbers) - 1)
    print("Removed from end:", removed)
    print("Updated list:", numbers)

    # ===============================
    # SEARCH TESTS
    # ===============================

    print("\n=== SEARCH TESTS ===")

    print("Current list:", numbers)

    # Search for a value that exists.
    value_to_find = 20
    result = search_value(numbers, value_to_find)

    if result != -1:
        print(
            value_to_find,
            "was found at index",
            result
        )
    else:
        print(value_to_find, "was not found.")

    # Search for a value that does not exist.
    missing_value = 100
    result = search_value(numbers, missing_value)

    if result != -1:
        print(
            missing_value,
            "was found at index",
            result
        )
    else:
        print(missing_value, "was not found in the list.")

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # Edge case 1:
    # Try deleting an index that does not exist.
    invalid_result = delete_at(numbers, 100)

    print("Deleting index 100:", invalid_result)
    print("List after invalid deletion:", numbers)

    # Edge case 2:
    # Insert a value into an empty list.
    empty_list = []

    print("\nEmpty list before insertion:", empty_list)

    insert_at(empty_list, 0, 99)

    print("Empty list after inserting 99:", empty_list)

    # Edge case 3:
    # Try deleting from an empty list.
    another_empty_list = []

    removed = delete_at(another_empty_list, 0)

    print("\nDeleting from an empty list:", removed)

    # ===============================
    # REAL-WORLD EXAMPLE
    # ===============================

    print("\n=== REAL-WORLD EXAMPLE ===")

    support_queue = [
        "Password reset",
        "Email problem",
        "Printer problem"
    ]

    print("Original support tickets:", support_queue)

    # A high priority ticket can be inserted near the front.
    insert_at(
        support_queue,
        1,
        "Network outage"
    )

    print(
        "After adding a priority ticket:",
        support_queue
    )

    # Search for a specific support request.
    ticket_index = search_value(
        support_queue,
        "Printer problem"
    )

    print(
        "Printer problem ticket index:",
        ticket_index
    )

    # Remove a completed ticket.
    completed_ticket = delete_at(support_queue, 0)

    print("Completed ticket:", completed_ticket)
    print("Remaining tickets:", support_queue)


if __name__ == "__main__":
    main()