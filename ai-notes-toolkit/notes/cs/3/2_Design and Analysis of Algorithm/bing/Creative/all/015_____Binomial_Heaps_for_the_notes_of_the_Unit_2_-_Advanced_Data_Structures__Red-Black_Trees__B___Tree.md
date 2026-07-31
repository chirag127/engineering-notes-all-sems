# Binomial Heaps

- A binomial heap is a data structure that acts as a priority queue but also allows pairs of heaps to be merged.
- A binomial heap is implemented as a set of binomial trees that satisfy the binomial heap properties:
  - Each binomial tree in a heap obeys the minimum-heap property: the key of a node is greater than or equal to the key of its parent.
  - There can be at most one binomial tree for each order, including zero order.
- A binomial tree of order 0 is a single node. A binomial tree of order k has a root node whose children are roots of binomial trees of orders k-1, k-2, ..., 2, 1, 0 (in this order).
- The number of nodes in a binomial tree of order k is 2^k. The height of a binomial tree of order k is k.
- A binomial heap supports the following operations in amortized logarithmic time :
  - **insert**: add a new node to the heap
  - **getMin**: return the node with the minimum key in the heap
  - **extractMin**: remove and return the node with the minimum key in the heap
  - **decreaseKey**: decrease the key of a given node in the heap
  - **delete**: remove a given node from the heap
  - **union**: merge two binomial heaps into one
- The union operation is the key to the efficiency of binomial heaps. It can be done by merging the lists of binomial trees of the two heaps and then rearranging the trees to maintain the binomial heap properties .
- The following diagram shows an example of a binomial heap with 13 nodes and four binomial trees of orders 0, 1, 2, and 3:

```
      1
    / | \
   2  3  4
  /|  |
 5 6  7
/| |\
8 9 10 11
        |
        12
        |
        13
```