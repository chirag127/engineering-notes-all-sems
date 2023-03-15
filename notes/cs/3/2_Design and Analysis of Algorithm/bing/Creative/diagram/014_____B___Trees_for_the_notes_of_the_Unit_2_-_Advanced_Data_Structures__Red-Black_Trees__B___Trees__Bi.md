Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some content on B-trees for the notes of the Unit 2 - Advanced Data Structures.

### B – Trees

- B-trees are a type of self-balancing tree data structure that maintain sorted data and allow efficient operations such as searches, insertions, and deletions in logarithmic time  .
- B-trees generalize the binary search trees by allowing nodes to have more than two children and more than one key  .
- B-trees are defined by a parameter called the minimum degree `t`, which is the minimum number of children a non-root node can have .
- B-trees have the following properties :
  - Every node has at most `2t` children and at least `t` children, except the root which can have fewer than `t` children but at least 2 children if it is not a leaf.
  - Every node has at most `2t-1` keys and at least `t-1` keys, except the root which can have fewer than `t-1` keys but at least 1 key if it is not a leaf.
  - The keys in each node are sorted in ascending order and act as separators for the subtrees.
  - The keys in the subtree rooted at the `i`-th child of a node are greater than the `i-1`-th key and less than or equal to the `i`-th key of the node.
  - All the leaves are at the same level, which is the height of the tree.
- B-trees are useful for storing large amounts of data that do not fit in main memory, such as databases and file systems, because they reduce the number of disk accesses required for operations  .
- B-trees support the following operations :
  - Search: To search for a key in a B-tree, we start from the root and compare the key with the keys in the node. If the key is found, we return the node and the index of the key. If the key is not found, we recursively search in the appropriate child subtree based on the separators. If the key is not present in the tree, we return null. The search operation takes `O(log n)` time, where `n` is the number of keys in the tree.
  - Insert: To insert a key in a B-tree, we first search for the key and if it is already present, we do nothing. Otherwise, we find the leaf node where the key should be inserted and insert the key in the node. If the node is not full, we are done. If the node is full, we split the node into two nodes and move the middle key to the parent node. We repeat this process until we reach a node that is not full or the root. If the root is full, we create a new root with the middle key and make the old root and the new node its children. The insert operation takes `O(log n)` time, where `n` is the number of keys in the tree.
  - Delete: To delete a key from a B-tree, we first search for the key and if it is not present, we do nothing. Otherwise, we find the node that contains the key and delete the key from the node. If the node is a leaf and has at least `t` keys, we are done. If the node is a leaf and has less than `t` keys, we try to borrow a key from its sibling or merge it with its sibling and delete the separator key from the parent node. We repeat this process until we reach a node that has at least `t` keys or the root. If the root has only one key and two children, we make the root the child that has at least `t` keys and delete the old root. The delete operation takes `O(log n)` time, where `n` is the number of keys in the tree.