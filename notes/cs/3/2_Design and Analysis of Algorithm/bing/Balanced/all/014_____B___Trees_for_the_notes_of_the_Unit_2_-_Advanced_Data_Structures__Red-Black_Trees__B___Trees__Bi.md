# B-Trees

- A B-tree is a **self-balancing** tree data structure that maintains **sorted** data and allows **searches, sequential access, insertions, and deletions** in logarithmic time   .
- A B-tree generalizes the binary search tree, allowing for nodes with more than two children  .
- A B-tree of order m has the following properties  :
  - Each node can have up to m children and m-1 keys.
  - Each node must have at least ⌈m/2⌉ children (except the root).
  - The root must have at least 2 children (unless it is a leaf).
  - All the leaves must be at the same level.
  - The keys in each node must be in ascending order and act as separators for the subtrees.
- The height of a B-tree of order m with n keys is O(logm n) .
- The search operation in a B-tree is similar to the binary search tree, but instead of comparing the key with one value, it compares with m-1 values in each node .
- The insertion operation in a B-tree involves finding the appropriate leaf node to insert the key and splitting the node if it is full .
- The deletion operation in a B-tree involves finding the key to delete and replacing it with its predecessor or successor if it is in an internal node, and merging or borrowing nodes if they become underfull .
- B-trees are widely used in **database systems** and **file systems** to store and retrieve large amounts of data efficiently  .