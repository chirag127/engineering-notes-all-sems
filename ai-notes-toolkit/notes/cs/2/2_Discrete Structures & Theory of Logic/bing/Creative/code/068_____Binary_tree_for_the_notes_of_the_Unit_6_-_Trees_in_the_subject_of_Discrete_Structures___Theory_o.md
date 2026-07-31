### Binary tree

A binary tree is a tree data structure where each node has at most two child nodes, creating the branches of the tree. The two children are usually called the left and right nodes .

A binary tree is also a rooted tree that is also an ordered tree (a.k.a. plane tree) in which every node has at most two children. A rooted tree naturally imparts a notion of levels (distance from the root), thus for every node a notion of children may be defined as the nodes connected to it a level below.

A binary tree can be represented by a pointer to the topmost node (commonly known as the “root”) of the tree. The root node has a data field and two pointers, one for the left child and one for the right child. If a node has no child, the corresponding pointer is set to null.

A binary tree can be classified into different types based on the number of children of each node:

- A full binary tree (sometimes referred to as a proper or plane or strict binary tree) is a tree in which every node has either 0 or 2 children. Another way of defining a full binary tree is a recursive definition. A full binary tree is either: A single vertex. A tree whose root node has two subtrees, both of which are full binary trees.
- A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.
- A perfect binary tree is a binary tree in which all interior nodes have two children and all leaves have the same depth or same level.
- A balanced binary tree is a binary tree in which the height of the left and right subtrees of every node differ by at most 1.
- A degenerate (or pathological) binary tree is a tree where every internal node has one child. Such trees are performance-wise same as linked list.

Some examples of binary trees are shown below:

```
    A full binary tree

        1
       / \
      2   3
     / \ / \
    4  5 6  7

    A complete binary tree

        1
       / \
      2   3
     / \ / 
    4  5 6  

    A perfect binary tree

        1
       / \
      2   3
     / \ / \
    4  5 6  7

    A balanced binary tree

        1
       / \
      2   3
     /   / \
    4   5   6

    A degenerate binary tree

        1
         \
          2
           \
            3
             \
              4
```

Some properties of binary trees are:

- The maximum number of nodes at level `l` of a binary tree is `2^l`. Here level is the number of nodes on the path from the root to the node (including the root and the node). Level of the root is 0.
- The maximum number of nodes in a binary tree of height `h` is `2^(h+1) - 1`. Here height of a node is the number of edges on the longest path from the node to a leaf. Height of the root is 0.
- In a binary tree with `n` nodes, the minimum possible height or the minimum number of levels is `log2(n+1)`.
- A binary tree with `l` leaves has at least `log2(l) + 1` levels.
- In a full binary tree, the number of leaf nodes is one more than the number of internal nodes.

Some applications of binary trees are:

- Binary trees are used to implement binary search trees and binary heaps, which are efficient data structures for searching and sorting data.
- Binary trees are used to construct optimal prefix codes, such as Huffman codes, which are widely used for data compression.
- Binary trees are used to represent arithmetic expressions and evaluate them using tree traversal algorithms.
- Binary trees are used to implement syntax trees, which are used by compilers and interpreters to parse and execute programming languages.
- Binary trees are used to implement decision trees, which are used for artificial intelligence and machine learning.