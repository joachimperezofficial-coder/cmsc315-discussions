"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


class Queue:

    def __init__(self):
        self.items = deque()

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):

        if self.is_empty():
            return None
        return self.items.popleft()

    def front(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # STACK DEMO
    # ===============================

    print("\n=== STACK DEMO ===")

    help_desk_stack = Stack()

    stack_actions = [
        "Open ticket",
        "Assign technician",
        "Add troubleshooting note",
        "Close ticket",
    ]

    print("\nAdding actions to the stack:")
    for action in stack_actions:
        help_desk_stack.push(action)
        print("Pushed:", action)

    print("\nTop value before removal:", help_desk_stack.peek())

    first_popped = help_desk_stack.pop()
    second_popped = help_desk_stack.pop()

    print("Popped first:", first_popped)
    print("Popped second:", second_popped)

    print(
        "\nLIFO explanation: "
        "The last action added was removed first."
    )

    # Test pop() and peek() on an empty stack.
    empty_stack = Stack()

    print("\nEmpty stack edge case:")
    print(
        "Result of pop() on an empty stack:",
        empty_stack.pop(),
    )
    print(
        "Result of peek() on an empty stack:",
        empty_stack.peek(),
    )

    # Test a stack containing only one item.
    single_item_stack = Stack()
    single_item_stack.push("Only stack item")

    print("\nSingle-item stack test:")
    print("Item removed:", single_item_stack.pop())
    print(
        "Is the stack empty after removal?",
        single_item_stack.is_empty(),
    )

    # ===============================
    # QUEUE DEMO
    # ===============================

    print("\n=== QUEUE DEMO ===")

    help_desk_queue = Queue()

    support_tickets = [
        "Ticket 101 - Password reset",
        "Ticket 102 - Wi-Fi issue",
        "Ticket 103 - Email issue",
        "Ticket 104 - Printer issue",
    ]

    print("\nAdding tickets to the queue:")
    for ticket in support_tickets:
        help_desk_queue.enqueue(ticket)
        print("Enqueued:", ticket)

    print(
        "\nFront value before removal:",
        help_desk_queue.front(),
    )

    first_removed = help_desk_queue.dequeue()
    second_removed = help_desk_queue.dequeue()

    print("Dequeued first:", first_removed)
    print("Dequeued second:", second_removed)

    print(
        "\nFIFO explanation: "
        "The first ticket added was removed first."
    )

    # Test dequeue() and front() on an empty queue.
    empty_queue = Queue()

    print("\nEmpty queue edge case:")
    print(
        "Result of dequeue() on an empty queue:",
        empty_queue.dequeue(),
    )
    print(
        "Result of front() on an empty queue:",
        empty_queue.front(),
    )

    # Test a queue containing only one item.
    single_item_queue = Queue()
    single_item_queue.enqueue("Only queue item")

    print("\nSingle-item queue test:")
    print("Item removed:", single_item_queue.dequeue())
    print(
        "Is the queue empty after removal?",
        single_item_queue.is_empty(),
    )

    # =====================================================
    # REAL-WORLD EXAMPLE
    # =====================================================

    print("\n=== REAL-WORLD EXAMPLE ===")
    print(
        "A help desk can use FIFO for incoming tickets "
        "and LIFO for recent actions."
    )

if __name__ == "__main__":
    main()
