### Binary tree traversal

- A binary tree is a non-linear data structure that stores data in the form of nodes, and nodes are connected to each other with the help of edges.
- A binary tree has one main node called the root node, and all other nodes are the children of these nodes.
- A binary tree traversal is a process of visiting each node in the tree exactly once in a predefined order.
- There are three common types of binary tree traversal: inorder, preorder and postorder.
- Inorder traversal: visit the left subtree, then the root, then the right subtree.
- Preorder traversal: visit the root, then the left subtree, then the right subtree.
- Postorder traversal: visit the left subtree, then the right subtree, then the root.
- A binary tree traversal can be implemented using recursion or iteration.
- A binary tree traversal can be used for various purposes, such as searching, sorting, printing, copying, deleting, etc.
- A binary tree traversal can also be done in a vertical order, where nodes at the same horizontal distance from the root are clustered together and output their depth in ascending order.

Here is an example of a binary tree and its inorder, preorder, postorder and vertical order traversal:

```
    1
   / \
  2   3
 / \   \
4   5   6
```

- Inorder traversal: 4 2 5 1 3 6
- Preorder traversal: 1 2 4 5 3 6
- Postorder traversal: 4 5 2 6 3 1
- Vertical order traversal: 4 2 1 5 3 6