### Binary search tree

- A binary search tree (BST) is a rooted binary tree data structure with the following properties :
  - The key of each node is greater than all the keys in its left subtree and less than all the keys in its right subtree.
  - The left and right subtrees of each node are also binary search trees.
  - There are no duplicate keys in the tree.
- A binary search tree supports the following operations in logarithmic time on average :
  - Search: find a node with a given key in the tree, or report that it does not exist.
  - Insert: add a new node with a given key and value to the tree, maintaining the BST property.
  - Delete: remove a node with a given key from the tree, maintaining the BST property.
  - Traverse: visit all the nodes in the tree in a specified order, such as in-order, pre-order, or post-order.
- A binary search tree can be represented by an array, a linked list, or a pointer-based structure .
- A binary search tree can be balanced or unbalanced, depending on how the nodes are distributed in the tree .
  - A balanced BST has a height that is logarithmic in the number of nodes, which ensures optimal performance of the operations.
  - An unbalanced BST can have a height that is linear in the number of nodes, which degrades the performance of the operations to linear time.
  - There are various algorithms to balance a BST, such as rotations, red-black trees, AVL trees, etc.

Here is an example of a binary search tree with 9 nodes:

```
      15
     /  \
    10   20
   / \   / \
  8  12 16  25
 / \
6   9
```

: Binary search tree - Wikipedia
: Binary Search Tree - GeeksforGeeks
: Binary Search Trees - Princeton University