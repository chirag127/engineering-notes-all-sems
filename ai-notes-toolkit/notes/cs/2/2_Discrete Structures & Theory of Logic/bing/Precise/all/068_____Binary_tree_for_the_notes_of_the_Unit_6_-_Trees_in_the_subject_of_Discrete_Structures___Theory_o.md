# Binary Tree

A binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.

## Properties of Binary Trees
- The maximum number of nodes at level `l` of a binary tree is `2^l`.
- The maximum number of nodes in a binary tree of height `h` is `2^h - 1`.
- In a non-empty binary tree with `n` nodes, there are `n+1` null links (empty sub-trees).
- A binary tree with `n` leaves has at least `log2(n) + 1` levels.
- A binary tree with `L` leaves has at least `|L| - 1` internal nodes.

## Types of Binary Trees
- **Full Binary Tree**: A binary tree in which every node has either 0 or 2 children.
- **Complete Binary Tree**: A binary tree in which all levels are completely filled except possibly the last level and the last level has all keys as left as possible.
- **Perfect Binary Tree**: A binary tree in which all internal nodes have two children and all leaves are at the same level.
- **Balanced Binary Tree**: A binary tree in which the height of the left and right subtrees of every node differ by at most 1.
- **Degenerate (or pathological) tree**: A tree where every internal node has one child.

## Traversals
- **Inorder Traversal**: Left subtree, root, right subtree.
- **Preorder Traversal**: Root, left subtree, right subtree.
- **Postorder Traversal**: Left subtree, right subtree, root.
- **Level Order Traversal**: Traverse level by level, from left to right.

## Applications
- Binary trees are used in many algorithms and data structures, such as binary search trees, heaps, and Huffman coding.
- They are also used in computer graphics, databases, and compilers.
