## Unit 2 - Advanced Data Structures: Red-Black Trees, B – Trees, Binomial Heaps, Fibonacci Heaps, Tries, Skip List

- Advanced data structures are data structures that provide more efficient ways to organize, store, and manipulate data than the basic data structures such as arrays, linked lists, stacks, queues, etc.
- Some of the advanced data structures are:

  - **Red-Black Trees**: A red-black tree is a type of self-balancing binary search tree, where each node has an extra bit that represents its color, either red or black. The tree maintains the following properties:
    - Every node is either red or black.
    - The root and the leaves (NIL) are black.
    - If a node is red, then both its children are black.
    - Every simple path from a node to a descendant leaf contains the same number of black nodes.
  - These properties ensure that the tree remains balanced, and the height of the tree is O(log n), where n is the number of nodes. The operations of insertion, deletion, and search can be performed in O(log n) time.

  - **B-Trees**: A B-tree is a type of multi-way search tree, where each node can have more than two children. The tree maintains the following properties:
    - All the leaves are at the same level.
    - Each node, except the root and the leaves, has at least t children, where t is a fixed integer greater than 1.
    - Each node, except the root, has at most 2t children.
    - Each node, except the leaves, has one key less than the number of its children, and the keys are stored in sorted order.
  - B-trees are useful for storing large amounts of data that do not fit in main memory, and can be accessed efficiently by disk operations. The operations of insertion, deletion, and search can be performed in O(log n) time, where n is the number of keys.

  - **Binomial Heaps**: A binomial heap is a type of heap data structure, where the heap is represented as a collection of binomial trees. A binomial tree of order k is a recursive structure that has the following properties:
    - It has 2^k nodes.
    - It has k levels, numbered from 0 to k-1.
    - The root has the smallest key among all the nodes in the tree, and the key of any node is greater than or equal to the key of its parent.
    - The root has k children, and the i-th child is a binomial tree of order k-i-1, for i = 0, 1, ..., k-1.
  - A binomial heap maintains the following properties:
    - Each binomial tree in the heap obeys the min-heap property, that is, the key of any node is greater than or equal to the key of its parent.
    - There can be at most one binomial tree of any order in the heap.
  - Binomial heaps are useful for implementing priority queues, as they support the operations of insert, delete-min, merge, and decrease-key in O(log n) time, where n is the number of nodes in the heap.

  - **Fibonacci Heaps**: A Fibonacci heap is a type of heap data structure, where the heap is represented as a collection of rooted trees that are not necessarily binomial. A Fibonacci heap maintains the following properties:
    - Each tree in the heap obeys the min-heap property, that is, the key of any node is greater than or equal to the key of its parent.
    - There is a pointer to the tree with the minimum key in the heap, called the min-pointer.
    - Each node has a degree, which is the number of its children, and a mark, which is a boolean value that indicates whether the node has lost a child since it became a child of another node.
    - The degree of any node is bounded by O(log n), where n is the number of nodes in the heap.
  - Fibonacci heaps are useful for implementing priority queues, as they support the operations of insert, delete-min, merge, and decrease-key in O(1) amortized time, and the operation of delete in O(log n) amortized time.

  - **Tries**: A trie is a type of tree data structure, where each node represents a prefix of a string