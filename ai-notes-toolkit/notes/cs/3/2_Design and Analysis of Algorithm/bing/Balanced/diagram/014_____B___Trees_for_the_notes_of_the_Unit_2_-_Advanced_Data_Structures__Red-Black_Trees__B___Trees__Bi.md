### B – Trees

B-trees are a type of self-balancing tree data structure that maintain sorted data and allow efficient operations such as searches, insertions, and deletions in logarithmic time. B-trees generalize the binary search tree, allowing for nodes with more than two children. B-trees are also known as height-balanced m-way trees or large key trees.

Some properties of B-trees are:

- A B-tree has a minimum degree `t` that determines the minimum and maximum number of keys and children in a node.
- A B-tree of degree `t` has the following characteristics:
  - Every node, except the root, has at least `t-1` keys and at most `2t-1` keys.
  - Every node, except the leaf nodes, has at least `t` children and at most `2t` children.
  - The root node has at least one key and at most `2t-1` keys. It has no children if it is the only node in the tree, otherwise it has at least two children.
  - All the leaf nodes are at the same level, which is the height of the tree.
  - The keys in a node are stored in sorted order, and the keys in the subtree of a key are either greater than or equal to (for the left subtree) or less than (for the right subtree) that key.
- The basic operations on a B-tree are:
  - Search: To search for a key in a B-tree, we start from the root node and compare the key with the keys in the node. If the key is found, we return the node and the index of the key. If the key is not found, we recursively search in the appropriate child of the node, based on the comparison result. The search operation takes `O(log n)` time, where `n` is the number of keys in the tree.
  - Insert: To insert a key in a B-tree, we first search for the key and find the leaf node where the key should be inserted. If the leaf node has less than `2t-1` keys, we simply insert the key in the node in sorted order. If the leaf node is full, we split the node into two nodes and move the middle key to the parent node, creating a new child pointer. This may cause the parent node to become full, in which case we repeat the splitting process until we reach a node that is not full or the root node. The insert operation takes `O(log n)` time, where `n` is the number of keys in the tree.
  - Delete: To delete a key from a B-tree, we first search for the key and find the node that contains the key. If the key is in a leaf node, we simply remove the key from the node. If the key is in an internal node, we replace the key with its predecessor (the rightmost key in the left subtree) or its successor (the leftmost key in the right subtree) and delete the predecessor or successor from the leaf node. In both cases, if the node has less than `t-1` keys after the deletion, we perform a balancing operation to ensure that the node has at least `t-1` keys. The balancing operation may involve borrowing a key from a sibling node or merging two sibling nodes and moving a key from the parent node. This may cause the parent node to have less than `t-1` keys, in which case we repeat the balancing process until we reach a node that has at least `t-1` keys or the root node. The delete operation takes `O(log n)` time, where `n` is the number of keys in the tree.

A diagram of a B-tree of degree 3 is shown below:

```
            +---+---+---+
            | 8 | 16|   |
            +---+---+---+
           /    |    |    \
          /     |    |     \
+---+---+---+  +---+---+---+  +---+---+---+  +---+---+---+
| 1 | 3 | 5 |  | 9 | 12| 14|  | 17| 19| 21|  | 24| 27| 30|
+---+---+---+  +---+---+---+  +---+---+---+  +---+---+---+
```