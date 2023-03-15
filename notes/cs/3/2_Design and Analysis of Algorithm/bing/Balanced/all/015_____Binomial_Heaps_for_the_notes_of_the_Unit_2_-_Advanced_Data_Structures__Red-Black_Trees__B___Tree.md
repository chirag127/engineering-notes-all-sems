# Binomial Heaps

- A binomial heap is a data structure that acts as a priority queue but also allows pairs of heaps to be merged.
- A binomial heap is implemented as a set of binomial trees that satisfy the binomial heap properties:
  - Each binomial tree in a heap obeys the minimum-heap property: the key of a node is greater than or equal to the key of its parent.
  - There can be at most one binomial tree for each order, including zero order.
- A binomial tree of order 0 is a single node. A binomial tree of order k has a root node whose children are roots of binomial trees of orders k-1, k-2, ..., 2, 1, 0 (in this order).
- The number of nodes in a binomial tree of order k is 2^k. The height of a binomial tree of order k is k.
- The binomial heap operations are as follows:
  - Create: create an empty binomial heap.
  - Insert: insert a new node into the binomial heap by creating a binomial tree of order 0 and merging it with the existing heap.
  - Get Minimum: find the root node with the minimum key in the binomial heap by scanning the roots of all binomial trees.
  - Extract Minimum: remove the root node with the minimum key from the binomial heap by deleting it and merging its children with the existing heap.
  - Union: merge two binomial heaps into one by combining the binomial trees of the same order and adjusting the heap property.
  - Decrease Key: decrease the key of a given node in the binomial heap by swapping it with its parent until the heap property is restored.
  - Delete: delete a given node from the binomial heap by decreasing its key to negative infinity and extracting the minimum.