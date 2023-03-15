# Implementation of Tree Structures, Binary Tree, Tree Traversal, Binary Search Tree, Insertion and Deletion in BST for the notes of the Data Structure using C Lab in the subject of Data Structure using C

## Tree Structures
- A tree is a nonlinear data structure that consists of nodes connected by edges.
- A tree has a root node, which is the topmost node in the hierarchy.
- A node can have zero or more child nodes, which are nodes that are directly connected to it by an edge.
- A node that has no child nodes is called a leaf node.
- A node that has at least one child node is called an internal node or a non-leaf node.
- The height of a node is the number of edges on the longest path from the node to a leaf node.
- The height of a tree is the height of the root node.
- The depth of a node is the number of edges on the path from the node to the root node.
- The depth of a tree is the depth of the deepest node in the tree.
- A subtree of a node is the tree formed by the node and all its descendants.
- A binary tree is a special kind of tree in which each node can have at most two child nodes, called the left child and the right child.

## Binary Tree
- A binary tree can be implemented using a dynamic data structure, such as a linked list, or a static data structure, such as an array.
- A linked list implementation of a binary tree uses a node structure that contains three fields: data, left pointer, and right pointer.
- The data field stores the value of the node, and the left and right pointers point to the left and right child nodes, respectively.
- The root node is stored in a separate pointer variable, and the left and right pointers of a leaf node are set to NULL.
- An array implementation of a binary tree uses an array of fixed size to store the nodes of the tree.
- The array is indexed from 1 to n, where n is the number of nodes in the tree.
- The root node is stored at index 1, and the left and right child nodes of a node at index i are stored at index 2i and 2i+1, respectively.
- The array elements that do not correspond to any node are left empty or filled with a special value, such as -1.

## Tree Traversal
- Tree traversal is the process of visiting each node of a tree in a systematic order.
- There are three common ways of traversing a binary tree: inorder, preorder, and postorder.
- Inorder traversal visits the left subtree, the root, and the right subtree of each node in that order.
- Preorder traversal visits the root, the left subtree, and the right subtree of each node in that order.
- Postorder traversal visits the left subtree, the right subtree, and the root of each node in that order.
- Tree traversal can be implemented using recursion or iteration.
- A recursive implementation of tree traversal uses a function that calls itself to visit the left and right subtrees of each node.
- An iterative implementation of tree traversal uses a stack or a queue to store the nodes that need to be visited.

## Binary Search Tree
- A binary search tree (BST) is a special kind of binary tree that satisfies the following property: the value of each node is greater than or equal to the values of all the nodes in its left subtree, and less than or equal to the values of all the nodes in its right subtree.
- A BST can be used to implement a sorted data structure that supports efficient search, insertion, and deletion operations.
- To search for a value in a BST, we start from the root node and compare the value with the node's value. If they are equal, we have found the node. If the value is less than the node's value, we search in the left subtree. If the value is greater than the node's value, we search in the right subtree. We repeat this process until we find the node or reach a leaf node.
- To insert a value in a BST, we follow the same procedure as search, but instead of returning the node, we create a new node with the value and attach it as the left or right child of the leaf node where the search ended.
- To delete a value from a BST, we first search for the node that contains the value. If the node is not found, we do nothing. If the node is found, we have three cases to consider:
  - If the node is a leaf node, we simply delete