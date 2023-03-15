### Binary search tree

- A binary search tree (BST) is a special type of binary tree that satisfies the following properties:
  - The left subtree of a node contains only nodes with keys less than the node's key.
  - The right subtree of a node contains only nodes with keys greater than the node's key.
  - The left and right subtrees of a node are also BSTs.
  - There are no duplicate keys in a BST.
- A BST supports efficient operations such as search, insert, delete, minimum, maximum, successor, and predecessor, which take O(h) time, where h is the height of the tree.
- A BST can be represented by an array, where the root node is at index 0, and the left and right children of a node at index i are at indices 2i+1 and 2i+2, respectively.
- A BST can also be represented by a linked list, where each node has a key, a data, a left pointer, and a right pointer.
- A BST can be traversed in different ways, such as preorder, inorder, postorder, and level order, which visit the nodes in different orders.
- A BST can be balanced or unbalanced, depending on how the nodes are distributed. A balanced BST has a height of O(log n), where n is the number of nodes, while an unbalanced BST can have a height of O(n) in the worst case.
- A BST can be balanced by using techniques such as rotation, splitting, joining, or using self-balancing BSTs such as AVL trees, red-black trees, or splay trees.