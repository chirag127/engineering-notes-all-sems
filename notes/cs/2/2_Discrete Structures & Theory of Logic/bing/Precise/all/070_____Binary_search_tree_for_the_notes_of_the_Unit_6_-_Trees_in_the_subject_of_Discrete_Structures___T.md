# Binary Search Tree

A binary search tree (BST) is a binary tree data structure where each node has at most two children, which are referred to as the left child and the right child. The key property of a binary search tree is that for every node, all elements in the left subtree are less than the node and all elements in the right subtree are greater than the node.

## Properties of a Binary Search Tree
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
- Each node has distinct key.

## Operations on a Binary Search Tree
- **Search**: To search for a value in a BST, we start from the root and compare the value with the root. If the value is less than the root, we search the left subtree. If the value is greater than the root, we search the right subtree. We repeat this process until we find the value or reach a leaf node.
- **Insertion**: To insert a value in a BST, we follow the same process as search. If the value is less than the current node, we go to the left subtree. If the value is greater than the current node, we go to the right subtree. When we reach a leaf node, we insert the new node as the left or right child of the leaf node.
- **Deletion**: To delete a node from a BST, we first search for the node. If the node has no children, we simply remove the node. If the node has one child, we replace the node with its child. If the node has two children, we find the inorder successor of the node, replace the node with the inorder successor, and delete the inorder successor.

## Advantages of Binary Search Tree
- Searching, insertion, and deletion operations are faster than in an unsorted array or linked list.
- Inorder traversal of a BST gives a sorted list of elements.
- BSTs can be used to implement sets, maps, and other abstract data types.

## Disadvantages of Binary Search Tree
- The shape of the BST depends on the order of insertion of elements. If the elements are inserted in sorted order, the BST becomes a skewed tree, which reduces its efficiency.
- The worst-case time complexity of search, insertion, and deletion operations is O(n), where n is the number of nodes in the tree.

## Applications of Binary Search Tree
- BSTs are used in many search applications where data is constantly entering and leaving.
- BSTs are used to implement sets, maps, and other abstract data types.
- BSTs are used in many algorithms such as Huffman coding and Dijkstra's algorithm.