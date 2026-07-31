### Binary search tree

- A binary search tree (BST) is a rooted binary tree data structure with the following properties :
  - The key of each node is greater than all the keys in its left subtree and less than all the keys in its right subtree.
  - The left and right subtrees of each node are also binary search trees.
  - There are no duplicate keys in the tree.
- A binary search tree supports the following operations in logarithmic time on average :
  - Search: find a node with a given key in the tree, or return null if not found.
  - Insert: add a new node with a given key and value to the tree, maintaining the BST property.
  - Delete: remove a node with a given key from the tree, maintaining the BST property.
  - Min: find the node with the smallest key in the tree.
  - Max: find the node with the largest key in the tree.
  - Predecessor: find the node with the largest key that is smaller than a given key.
  - Successor: find the node with the smallest key that is larger than a given key.
  - Inorder: traverse the nodes in the tree in ascending order of their keys.
- A binary search tree can be represented by an array, where the root node is at index 1, and the left and right children of a node at index i are at indices 2i and 2i+1, respectively.
- A binary search tree can also be represented by a linked list, where each node has a pointer to its left and right child, and optionally a pointer to its parent.
- A binary search tree can be balanced or unbalanced, depending on the shape of the tree. A balanced BST has a height that is logarithmic in the number of nodes, while an unbalanced BST can have a height that is linear in the number of nodes. A balanced BST can be achieved by using self-balancing algorithms, such as AVL trees, red-black trees, or splay trees .

: Binary search tree - Wikipedia
: Binary Search Tree - GeeksforGeeks
: Binary Search Trees - Princeton University