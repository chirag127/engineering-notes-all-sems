# Binary tree

- A binary tree is a **tree data structure** where each node has up to **two child nodes**, creating the branches of the tree  .
- The two children are usually called the **left and right nodes** .
- A binary tree is also a **rooted tree** that is also an **ordered tree** (a.k.a. plane tree) in which every node has at most two children.
- A rooted tree naturally imparts a notion of **levels** (distance from the root), thus for every node a notion of **children** may be defined as the nodes connected to it a level below.
- A binary tree is either:
  - An **empty tree** (a tree consisting of no vertices), or
  - A **non-empty tree** consisting of a **root node** and two subtrees that are both binary trees, called the **left subtree** and the **right subtree** of the root.
- A binary tree is called a **full binary tree** (sometimes referred to as a proper or plane or strict binary tree) if every node has either 0 or 2 children .
- A binary tree is called a **complete binary tree** if all levels are completely filled except possibly the last level and the last level has all keys as left as possible.
- A binary tree is called a **balanced binary tree** if the height of the tree is O(log n) where n is the number of nodes.
- A binary tree is called a **perfect binary tree** if all internal nodes have two children and all leaves are at the same level.
- A binary tree is called a **degenerate (or pathological) binary tree** if every internal node has one child. Such trees are performance-wise same as linked list.
- A binary tree is called a **skewed binary tree** if all nodes have only one child, either left or right.
- A binary tree is called a **binary search tree** if for every node, the value of all the nodes in the left subtree is lesser or equal and the value of all the nodes in the right subtree is greater or equal.
- A binary tree is called a **binary heap** if it is a complete binary tree and satisfies the heap property, which states that the value of a node is greater than or equal to (max-heap) or less than or equal to (min-heap) the value of its parent.
- A binary tree is called a **binary expression tree** if it is a binary tree that represents an arithmetic expression. Each internal node corresponds to an operator and each leaf node corresponds to an operand.
- A binary tree is called a **Huffman tree** if it is a binary tree that is used for optimal prefix coding. It is a full binary tree where each leaf node represents a character and its frequency, and the weight of each internal node is the sum of the weights of its children.