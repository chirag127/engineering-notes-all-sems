### B – Trees

A B-Tree is a self-balancing tree data structure that maintains sorted data and allows insertion, search, and deletion operations in O(log n) time complexity. It is commonly used in databases and file systems.

#### Structure of B-Tree

A B-Tree of order m has the following properties:

- Every node has at most m children.
- Every non-leaf node (except root) has at least ⌈m/2⌉ children.
- The root has at least two children if it is not a leaf node.
- A non-leaf node with k children contains k-1 keys.
- All leaves appear in the same level.

#### Insertion in B-Tree

The following steps are followed to insert a key in a B-Tree:

1. Traverse the tree to find the location to insert the key.
2. If the node is not full, insert the key in the node and keep it sorted.
3. If the node is full, split it into two nodes and move the median key to the parent node.
4. Repeat steps 2 and 3 recursively until the key is inserted.

#### Deletion in B-Tree

The following steps are followed to delete a key from a B-Tree:

1. Find the node containing the key to be deleted.
2. If the key is in a leaf node, delete it from the node.
3. If the key is in a non-leaf node, find the predecessor or successor key and replace the key to be deleted with it.
4. If the predecessor or successor node has less than ⌈m/2⌉ keys, merge it with a sibling node or redistribute keys between them.
5. Repeat steps 2-4 recursively until the key is deleted.

#### Advantages of B-Tree

- B-Tree is efficient for large datasets and high access rates.
- It supports insertion, deletion, and search operations in O(log n) time complexity.
- It is self-balancing, which guarantees good performance even with large datasets.

#### Disadvantages of B-Tree

- B-Tree has higher overhead compared to other data structures.
- It is complex to implement and maintain.
- It may not perform well for small datasets.

#### Example

Consider a B-Tree of order 3 with the following keys: 10, 20, 30, 40, 50, 60, 70, 80, 90.

```
              [40]
           /    |    \
       [20]  [60]  [80,90]
      /  |  \   |   /   \
  [10] [30] [50] [70]     [100]
```

If we want to insert 75 in the tree, the sequence of operations will be:

```
              [40]
           /    |    \
       [20]  [60]  [80,90]
      /  |  \   |   /   \
  [10] [30] [50] [70]  [100]

              [40]
           /    |    \
       [20]  [60]  [80,90]
      /  |  \   |   /   \
  [10] [30] [50] [70]  [75,100]

              [40]
           /    |    \
       [20]  [60]  [80]
      /  |  \   |   /   \
  [10] [30] [50] [70]  [75,90]

              [40]
           /    |    \
       [20,30] [60]  [80]
      /    |   \   /   \
  [10] [50] [70] [75]  [90]

              [40,70]
           /    |    \
       [20,30] [60]  [80]
      /         |   /   \
  [10]      [50] [75]  [90]
```

#### Applications of B-Tree

- B-Tree is commonly used in databases and file systems.
- It is also used in routers and switches for routing tables.
- B-Tree is useful for applications that require efficient searching and insertion of large datasets.