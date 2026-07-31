### B – Trees

- A B-tree is a **self-balancing** tree data structure that maintains **sorted** data and allows **searches, sequential access, insertions, and deletions** in logarithmic time   .
- A B-tree generalizes the binary search tree, allowing for nodes with more than two children .
- A B-tree of order m has the following properties :
  - Each node can have at most m children and m-1 keys.
  - Each node, except the root and the leaves, must have at least ⌈m/2⌉ children and ⌈m/2⌉-1 keys.
  - The root must have at least two children if it is not a leaf node.
  - All the leaves must be at the same level, and they have no children.
  - The keys in each node are stored in ascending order, and they act as separators for the subtrees.
  - A key k in a node N means that all the keys in the left subtree of N are less than k, and all the keys in the right subtree of N are greater than or equal to k.
- The height of a B-tree with n keys and order m is bounded by log<sub>m/2</sub>(n+1) and log<sub>m</sub>(n+1) .
- The basic operations on a B-tree are search, insert, and delete .
  - Search: To search for a key k in a B-tree, we start from the root and compare k with the keys in the current node. If k is found, we return the node and the index of k. If k is not found, we recursively search in the appropriate child subtree, or return null if there is no such child.
  - Insert: To insert a key k in a B-tree, we first search for the leaf node where k should be inserted. If the leaf node has less than m-1 keys, we simply insert k in the correct position and update the node. If the leaf node is full, we split it into two nodes and insert the middle key in the parent node, repeating the process until we reach a node that is not full or the root.
  - Delete: To delete a key k from a B-tree, we first search for the node that contains k. If k is in a leaf node, we simply remove it from the node and update the node. If k is in an internal node, we replace it with either its predecessor or successor in the tree, and then delete that key from the leaf node. If the deletion causes any node to have less than the minimum number of keys, we either borrow a key from a sibling node or merge two sibling nodes and delete a key from the parent node, repeating the process until we reach a node that satisfies the property or the root.
- B-trees are useful for storing and retrieving large amounts of data efficiently, especially when the data is stored on external memory devices such as disks   .
- B-trees are widely used in database systems, file systems, and indexing structures   .