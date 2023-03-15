## Unit 6 - Trees

A tree is a data structure that consists of a collection of nodes, each of which has a value and a list of references to other nodes called children. A node that has no children is called a leaf node. A node that has at least one child is called an internal node. A node that has no parent is called the root node. A tree can be empty, which means it has no nodes at all.

Some properties of trees are:

- A tree has exactly one root node, or none if it is empty.
- Every node except the root has exactly one parent.
- A node can have any number of children, from zero to many.
- There is a unique path from the root to every other node in the tree.
- The height of a tree is the length of the longest path from the root to any leaf node.
- The depth of a node is the length of the path from the root to that node.
- The level of a node is the depth of that node plus one.
- The degree of a node is the number of its children.
- The degree of a tree is the maximum degree of any node in the tree.

Some examples of trees are:

- A binary tree is a tree in which every node has at most two children, called the left child and the right child.
- A binary search tree is a binary tree in which the value of every node is greater than or equal to the value of its left child, and less than or equal to the value of its right child.
- A heap is a binary tree in which the value of every node is greater than or equal to the value of its children, or less than or equal to the value of its children, depending on whether it is a max-heap or a min-heap.
- A trie is a tree in which the value of every node is a character or a symbol, and the children of a node represent the possible continuations of the value of that node. A trie is often used to store words or strings in a compact and efficient way.
- A B-tree is a tree in which every node has a variable number of children, between a minimum and a maximum value, and the values of the nodes are stored in sorted order. A B-tree is often used to implement databases or file systems.

Some operations on trees are:

- Traversal: visiting every node in the tree in a certain order, such as pre-order, in-order, post-order, or level-order.
- Search: finding a node in the tree that has a given value, or finding the node that is closest to a given value.
- Insertion: adding a new node to the tree, while maintaining its properties and structure.
- Deletion: removing a node from the tree, while maintaining its properties and structure.
- Balancing: adjusting the shape of the tree to make it more balanced, which means reducing the difference between the heights of the subtrees of any node. A balanced tree can improve the performance of some operations, such as search, insertion, and deletion.