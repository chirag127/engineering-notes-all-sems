### Fibonacci Heaps

- A Fibonacci heap is a data structure for priority queue operations, consisting of a collection of heap-ordered trees  .
- A Fibonacci heap is a collection of trees satisfying the minimum-heap property, that is, the key of a child is always greater than or equal to the key of the parent. This implies that the minimum key is always at the root of one of the trees.
- Fibonacci heaps are named after the Fibonacci numbers, which are used in their running time analysis.
- For the Fibonacci heap, the find-minimum operation takes constant (O(1)) amortized time. The insert and decrease key operations also work in constant amortized time  .
- The delete and delete-minimum operations work in O(log n) amortized time, where n is the number of nodes in the heap  .
- The merge or union operation, which combines two Fibonacci heaps into one, works in constant amortized time  .
- The key advantage of a Fibonacci heap over other heap data structures is its fast amortized running time for operations such as insert, decrease key, and merge, which are useful in many algorithms such as Dijkstra's algorithm and Prim's algorithm  .
- The structure of a Fibonacci heap is more flexible than that of a binary heap or a binomial heap, as it allows arbitrary degree of nodes and arbitrary shape of trees.
- A Fibonacci heap maintains a pointer to the minimum node and a circular, doubly linked list of roots of the trees. Each node stores a pointer to its parent, a pointer to one of its children, and pointers to its left and right siblings. Each node also stores its degree (the number of children) and a mark bit (indicating whether it has lost a child since the last time it was made a child of another node) .
- A Fibonacci heap supports the following operations:

  - **make-heap**: creates and returns a new, empty Fibonacci heap.
  - **insert**: inserts a new node with a given key into the heap.
  - **find-min**: returns a pointer to the node with the minimum key in the heap.
  - **union**: merges two Fibonacci heaps into one and returns the resulting heap.
  - **extract-min**: deletes the node with the minimum key from the heap and returns its key.
  - **decrease-key**: decreases the key of a given node in the heap to a new value, which must be no greater than the current key.
  - **delete**: deletes a given node from the heap.