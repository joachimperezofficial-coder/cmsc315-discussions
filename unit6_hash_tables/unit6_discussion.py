"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

This program uses a Python dictionary to demonstrate
how a hash table stores, retrieves, updates, and removes
key-value pairs.

Real-world scenario:
A small store uses product SKUs as keys and the quantity
of each product in inventory as the value.
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # CREATE A HASH TABLE
    # ===============================

    # A Python dictionary behaves like a hash table.
    # Each SKU is a unique key, and its inventory quantity
    # is the value associated with that key.
    inventory = {}

    # Insert at least five key-value pairs.
    inventory["P100"] = 15
    inventory["P200"] = 8
    inventory["P300"] = 22
    inventory["P400"] = 5
    inventory["P500"] = 12

    print("\n=== INSERT OPERATIONS ===")
    print("Inventory after adding products:")
    print(inventory)

    # ===============================
    # LOOKUP OPERATIONS
    # ===============================

    # Dictionaries use the key to quickly locate its
    # associated value.
    print("\n=== LOOKUP OPERATIONS ===")

    print("P100 quantity:", inventory["P100"])
    print("P300 quantity:", inventory["P300"])

    # ===============================
    # UPDATE OPERATIONS
    # ===============================

    print("\n=== UPDATE OPERATIONS ===")

    print("Inventory before update:")
    print(inventory)

    # Assigning a new value to an existing key replaces
    # the old value instead of creating another key.
    inventory["P200"] = 20

    print("Inventory after updating P200:")
    print(inventory)

    # ===============================
    # DELETE OPERATIONS
    # ===============================

    print("\n=== DELETE OPERATIONS ===")

    print("Inventory before deletion:")
    print(inventory)

    # del removes both the key and its associated value.
    del inventory["P400"]

    print("Inventory after deleting P400:")
    print(inventory)

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # Edge Case 1:
    # get() safely looks up a key that may not exist.
    # Instead of causing an error, it returns None.
    missing_item = inventory.get("P999")
    print("Lookup for missing SKU P999:", missing_item)

    # Edge Case 2:
    # pop() with a default value safely attempts to remove
    # a missing key without causing a KeyError.
    removed_item = inventory.pop("P999", None)

    if removed_item is None:
        print("P999 was not removed because it does not exist.")
    else:
        print("P999 was removed.")

    # ===============================
    # REAL-WORLD SCENARIO
    # ===============================

    print("\n=== REAL-WORLD INVENTORY SCENARIO ===")

    # A store can quickly check whether a product exists
    # and retrieve the quantity using the product SKU.
    sku = "P300"

    if sku in inventory:
        print(
            sku,
            "is currently in stock with",
            inventory[sku],
            "items available."
        )
    else:
        print(sku, "is not currently in the inventory.")

    print("\nFinal inventory:")
    print(inventory)


if __name__ == "__main__":
    main()