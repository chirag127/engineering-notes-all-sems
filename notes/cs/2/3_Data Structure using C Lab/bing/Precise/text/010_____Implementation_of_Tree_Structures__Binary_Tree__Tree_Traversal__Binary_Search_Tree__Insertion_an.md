### Implementation of Tree Structures, Binary Tree, Tree Traversal, Binary Search Tree, Insertion and Deletion in BST for the notes of the Data Structure using C Lab in the subject of Data Structure using C

- **Tree Structures**: A tree is a non-linear data structure that consists of nodes connected by edges. Each node represents an element and the edges represent the relationship between the elements. The topmost node is called the root of the tree and the nodes with no children are called leaf nodes.

- **Binary Tree**: A binary tree is a special type of tree in which each node can have at most two children, commonly referred to as the left and right child. A binary tree can be empty, or it can contain a root node with left and right subtrees, which are also binary trees.

- **Tree Traversal**: Tree traversal refers to the process of visiting each node in a tree in a specific order. There are three common types of tree traversal: pre-order, in-order, and post-order. In pre-order traversal, the root is visited first, followed by the left subtree and then the right subtree. In in-order traversal, the left subtree is visited first, followed by the root and then the right subtree. In post-order traversal, the left subtree is visited first, followed by the right subtree and then the root.

- **Binary Search Tree**: A binary search tree (BST) is a binary tree in which the value of each node is greater than or equal to the values of all the nodes in its left subtree and less than or equal to the values of all the nodes in its right subtree. This property makes it possible to search for a specific value in a BST in O(log n) time, where n is the number of nodes in the tree.

- **Insertion in BST**: To insert a new value into a BST, we first compare it to the value of the root. If the new value is less than the root value, we insert it into the left subtree. If the new value is greater than the root value, we insert it into the right subtree. If the subtree where we need to insert the new value is empty, we create a new node with the new value and make it the root of the subtree.

- **Deletion in BST**: To delete a value from a BST, we first search for the node containing the value. If the node has no children, we simply remove it. If the node has one child, we replace the node with its child. If the node has two children, we find the node's in-order successor (the smallest value in its right subtree), replace the node with its in-order successor, and then delete the in-order successor from the right subtree.
