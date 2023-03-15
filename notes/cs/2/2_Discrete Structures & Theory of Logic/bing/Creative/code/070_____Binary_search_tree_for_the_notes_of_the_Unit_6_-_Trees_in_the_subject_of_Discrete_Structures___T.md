### Binary search tree

A binary search tree (BST) is a data structure that stores values in a hierarchical order. It has the following properties  :

- It is a rooted binary tree, which means it has a single node called the root at the top, and each node has at most two children, called the left child and the right child.
- The key of each node is comparable to the keys of other nodes, and it determines the order of the values in the tree.
- The key of each node is greater than all the keys in its left subtree and less than all the keys in its right subtree. This is called the binary search property.
- There is no duplicate key in the tree.

A BST can support efficient search, insertion, deletion, and traversal operations, as well as finding the minimum, maximum, predecessor, and successor of a given key. The average time complexity of these operations is O(log n), where n is the number of nodes in the tree, but the worst-case time complexity can be O(n) if the tree is skewed.

Here is an example of a BST with 7 nodes:

```
    8
   / \
  3   10
 / \    \
1   6    14
   / \   /
  4   7 13
```

: https://en.wikipedia.org/wiki/Binary_search_tree
: https://www.techopedia.com/definition/6282/binary-search-tree-bst
: https://www.geeksforgeeks.org/binary-search-tree-data-structure/