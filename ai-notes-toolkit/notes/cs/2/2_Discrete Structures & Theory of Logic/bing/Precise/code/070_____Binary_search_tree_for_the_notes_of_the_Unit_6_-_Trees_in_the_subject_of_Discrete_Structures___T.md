### Binary Search Tree

A binary search tree (BST) is a binary tree data structure that has the following properties:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

These properties ensure that the tree is ordered, allowing for efficient search, insertion, and deletion operations.

#### Search
To search for a value in a BST, we start at the root and compare the value to the root's key. If the value is less than the root's key, we search the left subtree. If the value is greater than the root's key, we search the right subtree. We repeat this process until we either find the value or reach a null node, indicating that the value is not in the tree.

#### Insertion
To insert a value into a BST, we follow the same process as for searching, but when we reach a null node, we create a new node with the value and insert it at that position.

#### Deletion
To delete a value from a BST, we first search for the node containing the value. If the node has no children, we simply remove it. If the node has one child, we replace the node with its child. If the node has two children, we find the node's in-order successor (the smallest value in the right subtree), replace the node with the in-order successor, and delete the in-order successor.

#### Complexity
The time complexity of search, insertion, and deletion operations in a BST is O(h), where h is the height of the tree. In the best case, the tree is balanced and the height is O(log n), where n is the number of nodes in the tree. In the worst case, the tree is skewed and the height is O(n).

#### Applications
BSTs are commonly used in computer science for searching and sorting algorithms. They are also used in databases to implement indexes and in compilers to implement symbol tables.