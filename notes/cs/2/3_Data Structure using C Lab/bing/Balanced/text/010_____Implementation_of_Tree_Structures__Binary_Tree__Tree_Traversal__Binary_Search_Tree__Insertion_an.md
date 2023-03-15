### Implementation of Tree Structures, Binary Tree, Tree Traversal, Binary Search Tree, Insertion and Deletion in BST for the notes of the Data Structure using C Lab in the subject of Data Structure using C

- A **tree structure** is a hierarchical data structure that consists of nodes, each having some data and possibly some children nodes.
- A **binary tree** is a special type of tree structure where each node can have at most two children, called the left child and the right child.
- **Tree traversal** is the process of visiting each node in a tree and performing some operation on it, such as printing its data or checking some condition.
- There are three common ways of traversing a binary tree: **inorder**, **preorder**, and **postorder**.
  - **Inorder traversal** visits the left subtree, then the root, and then the right subtree. This produces the nodes in sorted order for a binary search tree.
  - **Preorder traversal** visits the root, then the left subtree, and then the right subtree. This can be used to create a copy of the tree or to print a prefix expression of the tree.
  - **Postorder traversal** visits the left subtree, then the right subtree, and then the root. This can be used to delete the tree or to print a postfix expression of the tree.
- A **binary search tree (BST)** is a binary tree that satisfies the following property: the value of each node is greater than or equal to the values of all the nodes in its left subtree and less than or equal to the values of all the nodes in its right subtree.
- **Insertion** in a BST is the process of adding a new node with a given value to the tree, while maintaining the BST property. The algorithm is as follows:
  - Start from the root and compare the value to be inserted with the value of the root.
  - If the value is less than the root, then go to the left subtree. If the left subtree is empty, then create a new node with the value and make it the left child of the root. Otherwise, repeat the process with the left child as the new root.
  - If the value is greater than or equal to the root, then go to the right subtree. If the right subtree is empty, then create a new node with the value and make it the right child of the root. Otherwise, repeat the process with the right child as the new root.
- **Deletion** in a BST is the process of removing a node with a given value from the tree, while maintaining the BST property. The algorithm is as follows:
  - Search for the node with the given value in the tree. If the node is not found, then return.
  - If the node has no children, then simply delete the node and make its parent point to NULL.
  - If the node has one child, then replace the node with its child and delete the node.
  - If the node has two children, then find the inorder successor of the node, which is the smallest value in its right subtree. Copy the value of the inorder successor to the node and delete the inorder successor from the right subtree.