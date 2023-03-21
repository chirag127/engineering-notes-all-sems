### Definition for the notes of the Unit 6 - Trees in the subject of Discrete Structures & Theory of Logic

Trees are an essential data structure used in computer science and mathematics for representing hierarchical relationships between data. Trees are a type of graph, which consists of a set of vertices or nodes connected by edges. The main difference between trees and other graphs is that trees do not contain any cycles, making them acyclic graphs.

#### Basic Terminology

- **Node/Vertex:** A node is a fundamental unit of a tree that contains data and zero or more child nodes.
- **Edge:** An edge is a connection between two nodes that represents a relationship between the nodes.
- **Parent Node:** A node that has one or more child nodes is called a parent node.
- **Child Node:** A node that is directly connected to a parent node by an edge is called a child node.
- **Root Node:** The topmost node of a tree is called the root node. It has no parent node.
- **Leaf Node:** A node that has no child nodes is called a leaf node or a terminal node.
- **Path:** A path is a sequence of nodes and the edges between them.
- **Level:** The level of a node is the number of edges between the node and the root node. The root node is at level 0.
- **Height:** The height of a tree is the maximum level of any node in the tree.

#### Types of Trees

- **Binary Tree:** A binary tree is a tree in which each node has at most two children.
- **Full Binary Tree:** A full binary tree is a binary tree in which every node has either zero or two children.
- **Complete Binary Tree:** A complete binary tree is a binary tree in which all levels except possibly the last level are completely filled, and all nodes are as far left as possible.
- **Balanced Binary Tree:** A balanced binary tree is a binary tree in which the height of the left and right subtrees of any node differ by at most one.
- **Binary Search Tree:** A binary search tree is a binary tree in which for every node, the value of all nodes in the left subtree is less than the value of the node, and the value of all nodes in the right subtree is greater than the value of the node.

#### Tree Traversal

Tree traversal refers to the process of visiting all nodes of a tree in a specific order. There are three common methods of tree traversal:

- **Preorder Traversal:** In preorder traversal, we visit the root node first, followed by the left subtree and then the right subtree.
- **Inorder Traversal:** In inorder traversal, we visit the left subtree first, followed by the root node and then the right subtree.
- **Postorder Traversal:** In postorder traversal, we visit the left subtree first, followed by the right subtree and then the root node.

#### Applications of Trees

Trees have various applications in computer science and mathematics, including:

- Representing hierarchical relationships between data, such as file systems or organizational charts.
- Implementing data structures such as binary search trees or heaps.
- Representing syntax trees in compilers and interpreters.
- Solving various graph problems such as finding the shortest path or minimum spanning tree.