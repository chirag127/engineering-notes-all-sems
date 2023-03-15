### Binary search tree

- A binary search tree (BST) is a rooted binary tree data structure with the following properties :
  - The left subtree of a node contains only nodes with keys less than the node's key.
  - The right subtree of a node contains only nodes with keys greater than the node's key.
  - The key of each node is unique and comparable.
- A BST is also called an ordered or sorted binary tree, because it maintains a strict total order of the keys :
  - For any node, all the keys in its left subtree are smaller than its key, and all the keys in its right subtree are larger than its key.
  - This property is also called the binary search property, because it allows efficient search, insertion, and deletion operations on the BST.
- A BST can be represented by a linked list of nodes, where each node has a key, a value, and two pointers to its left and right children. Alternatively, a BST can be stored in an array, where the index of a node is its key, and the value is stored at that index. The left and right children of a node can be computed by adding or subtracting one from its index, respectively.
- A BST can be traversed in different ways, such as preorder, inorder, postorder, or level order. The most common traversal is inorder, which visits the nodes in ascending order of their keys. This can be done recursively or iteratively, using a stack to store the nodes to be visited.
- A BST can be constructed from a sorted array, by recursively choosing the middle element as the root, and dividing the array into two subarrays for the left and right subtrees. This can be done in O(n) time, where n is the number of elements in the array.
- A BST can be balanced, meaning that the height of the tree is O(log n), where n is the number of nodes. A balanced BST ensures that the search, insertion, and deletion operations take O(log n) time in the worst case. There are different ways to balance a BST, such as using rotations, or using self-balancing algorithms, such as AVL trees, red-black trees, or splay trees.