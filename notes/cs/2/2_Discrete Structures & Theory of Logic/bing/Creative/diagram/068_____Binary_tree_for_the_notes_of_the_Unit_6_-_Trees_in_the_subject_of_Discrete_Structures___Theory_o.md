### Binary tree

- A binary tree is a tree data structure where each node has at most two child nodes, creating the branches of the tree.
- The two children are usually called the left and right nodes.
- A binary tree is a rooted tree that is also an ordered tree (a.k.a. plane tree) in which every node has at most two children.
- A rooted tree naturally imparts a notion of levels (distance from the root), thus for every node a notion of children may be defined as the nodes connected to it a level below.
- A full binary tree (sometimes referred to as a proper or plane or strict binary tree) is a tree in which every node has either 0 or 2 children.
- Another way of defining a full binary tree is a recursive definition. A full binary tree is either: A single vertex. A tree whose root node has two subtrees, both of which are full binary trees.
- A binary tree is represented by a pointer to the topmost node (commonly known as the “root”) of the tree.
- Since each element in a binary tree can have only 2 children, we typically name them the left and right child.
- A binary tree can be empty, in which case it has no nodes and no root.
- A binary tree can also have only one node, which is the root, and no children.
- A binary tree can be traversed in different ways, such as pre-order, in-order, post-order, and level-order.
- A binary tree can have various properties and applications, such as height, depth, size, balance, search, insertion, deletion, sorting, etc.

Here is an example of a binary tree:

```
    A
   / \
  B   C
 / \   \
D   E   F
```

In this binary tree, A is the root, B and C are the left and right children of A, D and E are the left and right children of B, and F is the right child of C. The tree has 6 nodes, 5 edges, and 3 levels. The height of the tree is 2, and the depth of node F is 2. The tree is not a full binary tree, because node C has only one child. The tree can be traversed in different ways, such as:

- Pre-order: A, B, D, E, C, F
- In-order: D, B, E, A, C, F
- Post-order: D, E, B, F, C, A
- Level-order: A, B, C, D, E, F