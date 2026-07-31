# Implementation of Tree Structures, Binary Tree, Tree Traversal, Binary Search Tree, Insertion and Deletion in BST for the notes of the Data Structure using C Lab in the subject of Data Structure using C

## Tree Structures
- A tree is a non-linear data structure that represents hierarchical relationships between elements.
- Each element in a tree is called a node.
- The topmost node in a tree is called the root node.
- Nodes that are connected to the same parent node are called siblings.
- Nodes that do not have any children are called leaf nodes.

## Binary Tree
- A binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.
- A binary tree can be empty, or it can contain a root node and zero or more subtrees, each of which is also a binary tree.

## Tree Traversal
- Tree traversal is the process of visiting each node in a tree in a specific order.
- There are three common ways to traverse a binary tree: in-order, pre-order, and post-order.
- In-order traversal: visit the left subtree, then the root, then the right subtree.
- Pre-order traversal: visit the root, then the left subtree, then the right subtree.
- Post-order traversal: visit the left subtree, then the right subtree, then the root.

## Binary Search Tree
- A binary search tree (BST) is a binary tree in which the value of each node is greater than or equal to the values in its left subtree and less than or equal to the values in its right subtree.
- The left and right subtrees of a BST are also BSTs.

## Insertion and Deletion in BST
- To insert a new node into a BST, we first compare the value of the new node with the value of the root. If the value of the new node is less than the value of the root, we insert the new node into the left subtree. If the value of the new node is greater than the value of the root, we insert the new node into the right subtree.
- To delete a node from a BST, we first search for the node to be deleted. If the node has no children, we simply remove it. If the node has one child, we replace the node with its child. If the node has two children, we find the node's in-order successor, replace the node with its in-order successor, and then delete the in-order successor.
