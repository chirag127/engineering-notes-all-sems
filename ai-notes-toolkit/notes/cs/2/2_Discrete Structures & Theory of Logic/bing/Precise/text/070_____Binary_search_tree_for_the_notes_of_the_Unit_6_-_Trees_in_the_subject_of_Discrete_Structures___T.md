### Binary Search Tree

A binary search tree (BST) is a binary tree data structure where each node has at most two children, which are referred to as the left child and the right child. The key property of a binary search tree is that for every node, all elements in the left subtree are less than the node and all elements in the right subtree are greater than the node.

Here are some key points to remember about binary search trees:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
- Each node has distinct key.

Binary search trees are used for efficient searching and sorting of data. The average time complexity for search, insert, and delete operations in a binary search tree is O(log n), where n is the number of nodes in the tree.

Some common operations that can be performed on a binary search tree include:

- **Search**: To search for a value in a binary search tree, start at the root and compare the value to be searched with the value of the root. If the value is less than the root, search the left subtree. If the value is greater than the root, search the right subtree. Repeat the process until the value is found or the subtree being searched is empty.
- **Insert**: To insert a value into a binary search tree, start at the root and compare the value to be inserted with the value of the root. If the value is less than the root, insert the value into the left subtree. If the value is greater than the root, insert the value into the right subtree. Repeat the process until a leaf node is reached, and then add the new node as a child of the leaf node.
- **Delete**: To delete a value from a binary search tree, first search for the node containing the value to be deleted. If the node has no children, simply remove the node. If the node has one child, replace the node with its child. If the node has two children, find the in-order successor of the node, replace the node's value with the value of the in-order successor, and then delete the in-order successor.

These are some of the key concepts and operations related to binary search trees. They are an important data structure for efficient searching and sorting of data. It is important to understand the properties and operations of binary search trees in order to use them effectively.