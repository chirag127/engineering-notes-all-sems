### Implementation of Tree Structures, Binary Tree, Tree Traversal, Binary Search Tree, Insertion and Deletion in BST for the notes of the Data Structure using C Lab in the subject of Data Structure using C

#### Tree Structures
- A tree is a hierarchical data structure that consists of nodes connected by edges.
- Each node in a tree has a parent node and zero or more child nodes.
- The topmost node in a tree is called the root node.
- Nodes that have no children are called leaf nodes.

#### Binary Tree
- A binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.
- A binary tree can be empty or it can contain one or more nodes.
- A binary tree can be represented using an array or a linked list.

#### Tree Traversal
- Tree traversal is the process of visiting each node in a tree in a specific order.
- There are three common ways to traverse a binary tree: in-order, pre-order, and post-order.
- In-order traversal: visit the left subtree, then the root, then the right subtree.
- Pre-order traversal: visit the root, then the left subtree, then the right subtree.
- Post-order traversal: visit the left subtree, then the right subtree, then the root.

#### Binary Search Tree
- A binary search tree (BST) is a binary tree in which the value of each node is greater than or equal to the values in its left subtree and less than or equal to the values in its right subtree.
- The left and right subtrees of a BST are also BSTs.
- BSTs are commonly used to implement efficient search and sorting algorithms.

#### Insertion and Deletion in BST
- To insert a new value into a BST, we first compare the value to the root. If the value is less than the root, we insert it into the left subtree. If the value is greater than the root, we insert it into the right subtree.
- To delete a value from a BST, we first search for the value. If the value is not found, the deletion is unsuccessful. If the value is found, we have three cases to consider:
    1. The node containing the value has no children: we simply remove the node.
    2. The node containing the value has one child: we replace the node with its child.
    3. The node containing the value has two children: we find the node's in-order successor, replace the node with its in-order successor, and delete the in-order successor.
