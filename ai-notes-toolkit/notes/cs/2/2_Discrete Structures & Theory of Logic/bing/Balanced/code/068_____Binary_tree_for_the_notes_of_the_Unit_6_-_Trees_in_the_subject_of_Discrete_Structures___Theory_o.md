### Binary tree

A binary tree is a tree data structure where each node has at most two child nodes, creating the branches of the tree. The two children are usually called the left and right nodes . A binary tree is also a rooted tree that is an ordered tree (a.k.a. plane tree) in which every node has at most two children. A rooted tree naturally imparts a notion of levels (distance from the root), thus for every node a notion of children may be defined as the nodes connected to it a level below.

Some important properties of binary trees are:

- A binary tree is either empty or consists of a root node and two disjoint binary trees called the left subtree and the right subtree.
- The height of a binary tree is the maximum number of edges in a path from the root to a leaf.
- The number of nodes in a binary tree is at least one (if not empty) and at most 2^h, where h is the height of the tree.
- The number of leaf nodes in a binary tree is at least one and at most 2^(h/2), where h is the height of the tree.
- A full binary tree (sometimes referred to as a proper or plane or strict binary tree) is a tree in which every node has either 0 or 2 children. Another way of defining a full binary tree is a recursive definition. A full binary tree is either: A single vertex. A tree whose root node has two subtrees, both of which are full binary trees.
- A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

A binary tree can be represented in different ways, such as:

- Using a linked list, where each node has a data field and two pointers to its left and right children.
- Using an array, where the root node is stored at index 0 and the left and right children of a node at index i are stored at indices 2i+1 and 2i+2, respectively.
- Using a parenthesized expression, where each node is enclosed by parentheses and its left and right subtrees are separated by a comma.

An example of a binary tree and its different representations is shown below:

```
    A
   / \
  B   C
 / \   \
D   E   F

Linked list: A -> (B, C), B -> (D, E), C -> (NULL, F), D -> (NULL, NULL), E -> (NULL, NULL), F -> (NULL, NULL)

Array: [A, B, C, D, E, NULL, F, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL]

Parenthesized expression: (A (B (D) (E)) (C () (F)))
```