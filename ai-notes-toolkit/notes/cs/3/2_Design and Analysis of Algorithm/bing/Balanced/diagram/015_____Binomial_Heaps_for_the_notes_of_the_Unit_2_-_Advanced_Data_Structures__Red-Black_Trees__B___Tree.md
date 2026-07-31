### Binomial Heaps

- A binomial heap is a data structure that acts as a priority queue but also allows pairs of heaps to be merged.
- A binomial heap is implemented as a set of binomial trees that satisfy the binomial heap properties:
  - Each binomial tree in a heap obeys the minimum-heap property: the key of a node is greater than or equal to the key of its parent.
  - There can be at most one binomial tree for each order, including zero order.
- A binomial tree of order 0 is a single node. A binomial tree of order k has a root node whose children are roots of binomial trees of orders k-1, k-2, ..., 2, 1, 0 (in this order).
- The number of nodes in a binomial tree of order k is 2^k. The height of a binomial tree of order k is k.
- A binomial heap can support the following operations in O(log n) time, where n is the number of nodes in the heap :
  - Insert: add a new node to the heap as a binomial tree of order 0, then merge any trees of the same order until the heap property is restored.
  - Get Minimum: find the root node with the smallest key among all the binomial trees in the heap.
  - Extract Minimum: remove the root node with the smallest key from the heap, then add its children as separate binomial trees to the heap, then merge any trees of the same order until the heap property is restored.
  - Union: merge two binomial heaps into one by adding the corresponding binomial trees of the same order, then merge any trees of the same order until the heap property is restored.
  - Decrease Key: decrease the key of a given node in the heap, then swap it with its parent until the heap property is restored.
  - Delete: decrease the key of a given node to negative infinity, then extract the minimum node from the heap.

Here is an example of a binomial heap with 13 nodes and 4 binomial trees of orders 0, 1, 2, and 3:

```
      3
    / | \
   7  9  25
  /|  |  / \
 10 8  12 14
/|     |
11 15  18
```

: Binomial heap - Wikipedia
: Binomial Heap | Brilliant Math & Science Wiki
: Binomial Heap - GeeksforGeeks