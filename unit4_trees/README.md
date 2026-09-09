Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
   I learned how a Binary Search Tree organizes values and how recursion can be used for insertion, searching, and in-order traversal. I also learned that smaller values go to the left subtree while larger values go to the right. The in-order traversal helped me see how a BST can return values in sorted order.

2. What challenges did you encounter, and how did you overcome them?
The most challenging part was understanding how the recursive methods keep moving through the tree until they reach the correct node or an empty location. I worked through this by testing smaller examples and checking the output after insertion and search operations. I also tested empty trees and duplicate values to make sure the program handled edge cases correctly.

3. Explain BST behavior and compare how ordering creates efficiency compared with other data structures.
A BST uses ordering to reduce the amount of data that needs to be searched. After each comparison, the program can choose either the left or right subtree instead of checking every value. This can be more efficient than a linear search when the tree is balanced. However, if values are inserted in sorted order, the tree can become unbalanced and behave more like a linked list, which reduces its efficiency.