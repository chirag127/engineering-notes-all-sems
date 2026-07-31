### Binary Search Tree

A binary search tree (BST) is a binary tree data structure where each node has at most two children, which are referred to as the left child and the right child. The key property of a binary search tree is that for every node, all elements in the left subtree are less than the node and all elements in the right subtree are greater than the node.

Here are some key points to remember about binary search trees:

1. The left subtree of a node contains only nodes with keys less than the node's key.
2. The right subtree of a node contains only nodes with keys greater than the node's key.
3. Both the left and right subtrees must also be binary search trees.
4. Each node has distinct key.

Binary search trees are used for efficient searching and sorting of data. The average time complexity for search, insert, and delete operations in a binary search tree is O(log n), where n is the number of nodes in the tree.

However, in the worst case, the time complexity can be O(n) if the tree is not balanced. To avoid this, self-balancing binary search trees such as AVL trees or red-black trees can be used.

Here is an example of a binary search tree:

```
    8
   / \
  3   10
 / \    \
1   6    14
   / \   /
  4   7 13
```

In this tree, the root node is 8. The left subtree contains the nodes 3, 1, 6, 4, and 7, all of which have values less than 8. The right subtree contains the nodes 10, 14, and 13, all of which have values greater than 8. Each subtree is also a binary search tree.
