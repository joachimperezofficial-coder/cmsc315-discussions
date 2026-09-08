"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

This program demonstrates recursive insertion, searching,
in-order traversal, and edge cases using a BST.
"""


class Node:
    def __init__(self, value):
        # Each node stores a value and references to its
        # left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # An empty BST starts without a root node.
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BST.
        """
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        Recursively insert a value into the BST.
        """

        # When an empty position is found, create a new node.
        if node is None:
            return Node(value)

        # Smaller values belong in the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values belong in the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Duplicate values are ignored so each value appears once.
        return node

    def search(self, value):
        """
        Search for a value in the BST.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        Recursively search for a value.
        """

        # Reaching an empty position means the value was not found.
        if node is None:
            return False

        # The value has been found.
        if value == node.value:
            return True

        # BST ordering lets the search choose only one subtree.
        # This often reduces the amount of data that must be checked
        # compared with a linear search.
        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        Return the values using an in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        Recursively perform an in-order traversal.
        """

        if node is not None:
            # Visit the left subtree first.
            self._inorder_recursive(node.left, values)

            # Then visit the current node.
            values.append(node.value)

            # Finally visit the right subtree.
            self._inorder_recursive(node.right, values)

            # Because smaller values are stored on the left and
            # larger values are stored on the right, this produces
            # the values in sorted order.


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # BUILD A TREE
    # ===============================

    print("\n=== TREE CONSTRUCTION ===")

    tree = BST()

    # These values create both left and right subtrees.
    values = [50, 30, 70, 20, 40, 60, 80]

    print("Values inserted:")

    for value in values:
        tree.insert(value)
        print(value)

    # A BST can reduce the search space because each comparison
    # determines whether to continue left or right instead of
    # checking every value in sequence.

    # ===============================
    # IN-ORDER TRAVERSAL
    # ===============================

    print("\n=== IN-ORDER TRAVERSAL ===")

    traversal = tree.inorder()

    print("In-order traversal:", traversal)
    print("The values appear in sorted order because the traversal")
    print("visits the left subtree, current node, and right subtree.")

    # ===============================
    # SEARCH TESTS
    # ===============================

    print("\n=== SEARCH TESTS ===")

    # Existing values should return True.
    print("Search for 40:", tree.search(40))
    print("Search for 70:", tree.search(70))

    # Missing values should return False.
    print("Search for 25:", tree.search(25))
    print("Search for 90:", tree.search(90))

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # Searching an empty tree should return False.
    empty_tree = BST()
    print("Search empty tree for 10:", empty_tree.search(10))

    # Traversing an empty tree should return an empty list.
    print("Empty tree traversal:", empty_tree.inorder())

    # Duplicate values are ignored by this implementation.
    tree.insert(50)
    print("After inserting duplicate 50:", tree.inorder())

    # ===============================
    # REAL-WORLD EXAMPLE
    # ===============================

    print("\n=== REAL-WORLD EXAMPLE ===")
    print("A BST could be used to organize employee or product IDs.")
    print("The ordering allows the program to decide whether to")
    print("search the left or right subtree after each comparison.")


if __name__ == "__main__":
    main()
