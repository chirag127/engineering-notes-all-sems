### Implementation of Tree Structures, Binary Tree, Tree Traversal, Binary Search Tree, Insertion and Deletion in BST for the notes of the Data Structure using C Lab in the subject of Data Structure using C

- A tree data structure is a non-linear and hierarchical data structure that is a collection of multiple nodes connected by edges .
- A tree has a root node, which is the topmost node, and zero or more child nodes, which are the nodes below the root .
- A node that has no child is called a leaf node .
- A node that has at least one child is called an internal node .
- A node can have at most one parent, but can have multiple children .
- The height of a node is the number of edges from the node to the deepest leaf .
- The height of a tree is the height of the root node .
- The depth of a node is the number of edges from the root to the node .
- The degree of a node is the number of children of the node .
- The degree of a tree is the maximum degree of any node in the tree .

- A binary tree is a special type of tree data structure that has at most two children for each node .
- A binary tree can be empty, or it can have a root node and two subtrees, called the left subtree and the right subtree .
- A binary tree can be classified into different types, such as full binary tree, complete binary tree, perfect binary tree, balanced binary tree, etc .
- A full binary tree is a binary tree in which every node has either zero or two children .
- A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible .
- A perfect binary tree is a binary tree in which every node has two children and all leaves are at the same level .
- A balanced binary tree is a binary tree in which the height of the left and right subtrees of every node differ by at most one .

- Tree traversal is the process of visiting each node in a tree exactly once in a systematic way .
- There are different ways to traverse a tree, such as preorder, inorder, postorder, and level order .
- Preorder traversal is a recursive algorithm that visits the root node, then the left subtree, and then the right subtree .
- Inorder traversal is a recursive algorithm that visits the left subtree, then the root node, and then the right subtree .
- Postorder traversal is a recursive algorithm that visits the left subtree, then the right subtree, and then the root node .
- Level order traversal is an iterative algorithm that visits the nodes level by level, from left to right .

- A binary search tree (BST) is a binary tree that satisfies the following property: for every node, the value of the node is greater than or equal to the values of all the nodes in the left subtree, and less than or equal to the values of all the nodes in the right subtree .
- A BST can be used to implement a sorted set or a sorted map data structure .
- A BST supports efficient search, insertion, and deletion operations, as they can be done in O(h) time, where h is the height of the tree .
- The worst-case time complexity of BST operations is O(n), where n is the number of nodes in the tree, which happens when the tree is skewed .
- The best-case time complexity of BST operations is O(log n), where n is the number of nodes in the tree, which happens when the tree is balanced[^2^