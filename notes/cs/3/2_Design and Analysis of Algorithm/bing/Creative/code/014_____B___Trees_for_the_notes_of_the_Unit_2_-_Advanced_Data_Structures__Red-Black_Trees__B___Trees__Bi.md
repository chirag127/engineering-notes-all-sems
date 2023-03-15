### B-Trees

- A B-tree is a self-balancing tree data structure that maintains sorted data and allows searches, insertions, and deletions in logarithmic time  .
- A B-tree is optimized for systems that read and write large data blocks, unlike self-balancing binary search trees. It is commonly used in database and file management systems .
- A B-tree is a generalization of the binary search tree, allowing for nodes with more than two children . It is also known as a height-balanced m-way tree.
- A B-tree has the following properties   :
  - Every node has a maximum of m children, where m is the order of the tree.
  - Every node (except the root and the leaves) has a minimum of ⌈m/2⌉ children.
  - The root has a minimum of two children if it is not a leaf node.
  - All the leaves are at the same level, and they have no children.
  - Every non-leaf node with k children contains k-1 keys, which are sorted in ascending order.
  - The keys in a node act as separators for the subtrees. For a node with k-1 keys, the first subtree contains keys less than the first key, the second subtree contains keys between the first and the second key, and so on, and the last subtree contains keys greater than the last key.
- A B-tree supports the following operations   :
  - Search: To search for a key in a B-tree, we start from the root and compare the key with the keys in the node. If the key is found, we return the node. If the key is not found, we recursively search in the appropriate subtree based on the separators. The search operation takes O(log n) time, where n is the number of keys in the tree.
  - Insert: To insert a key in a B-tree, we first search for the leaf node where the key should be inserted. If the leaf node has space, we simply insert the key in the sorted order. If the leaf node is full, we split it into two nodes and insert the middle key in the parent node. This may cause the parent node to overflow, in which case we repeat the splitting process until we reach a node that has space or the root. The insert operation takes O(log n) time, where n is the number of keys in the tree.
  - Delete: To delete a key from a B-tree, we first search for the node that contains the key. If the key is in a leaf node, we simply remove it from the node. If the key is in a non-leaf node, we replace it with its predecessor or successor (which is in a leaf node) and then delete that key from the leaf node. After deleting a key, we may need to adjust the tree to maintain the B-tree properties. This may involve merging or redistributing nodes to ensure that every node (except the root) has at least ⌈m/2⌉ children. The delete operation takes O(log n) time, where n is the number of keys in the tree.