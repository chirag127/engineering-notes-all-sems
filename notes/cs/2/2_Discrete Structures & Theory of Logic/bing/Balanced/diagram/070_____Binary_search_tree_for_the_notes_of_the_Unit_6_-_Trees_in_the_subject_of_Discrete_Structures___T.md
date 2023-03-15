### Binary search tree

- A binary search tree (BST) is a rooted binary tree data structure with the following properties :
  - The key of each node is greater than all the keys in its left subtree and less than all the keys in its right subtree.
  - The left and right subtrees of each node are also binary search trees.
  - There are no duplicate keys in the tree.
- A binary search tree supports efficient search, insertion, and deletion operations, as well as traversal, minimum, maximum, and predecessor/successor queries.
- The worst-case time complexity of these operations is O(n), where n is the number of nodes in the tree, if the tree is unbalanced or degenerate (i.e., a linked list).
- The average-case and best-case time complexity of these operations is O(log n), if the tree is balanced or nearly balanced (i.e., the height is proportional to the logarithm of the number of nodes).
- A binary search tree can be implemented using pointers, arrays, or dynamic data structures such as linked lists or hash tables.
- A binary search tree can be represented graphically as follows, where each node is labeled with its key and the left and right subtrees are drawn below it:

```
      8
     / \
    3   10
   / \    \
  1   6    14
     / \   /
    4   7 13
```