### Fibonacci Heaps

- A Fibonacci heap is a data structure for priority queue operations, consisting of a collection of heap-ordered trees.
- A heap-ordered tree is a tree that satisfies the minimum-heap property, that is, the key of a child is always greater than or equal to the key of the parent.
- The minimum key is always at the root of one of the trees.
- The structure of a Fibonacci heap is more flexible than a binary heap or a binomial heap, allowing for faster amortized running time for some operations .
- A Fibonacci heap supports the following operations :
  - `find-min`: returns the root of the tree containing the minimum key in constant (O(1)) amortized time.
  - `insert`: adds a new node to the heap in constant (O(1)) amortized time.
  - `decrease-key`: decreases the key of a given node in the heap in constant (O(1)) amortized time.
  - `delete-min`: removes and returns the minimum node from the heap in O(log n) amortized time, where n is the number of nodes in the heap.
  - `delete`: removes a given node from the heap in O(log n) amortized time.
  - `merge`: combines two Fibonacci heaps into one in constant (O(1)) time .
- A Fibonacci heap is named after the Fibonacci numbers, which are used in its running time analysis.
- A Fibonacci heap is used to implement the priority queue element in Dijkstra’s algorithm, giving the algorithm a very efficient running time.
- A Fibonacci heap is represented as a circular doubly linked list of roots of the trees, with a pointer to the minimum node .
- The trees in a Fibonacci heap are not constrained by any shape or order, unlike a binary heap or a binomial heap .
- The trees in a Fibonacci heap are ranked by their degree, which is the number of children of the root .
- The degree of a tree in a Fibonacci heap is bounded by O(log n), where n is the number of nodes in the tree .
- The trees in a Fibonacci heap are marked to indicate whether they have lost a child since the last time they were made the child of another node .
- The marking of the trees is used to maintain the potential function of the heap, which is used to analyze the amortized running time of the operations .
- The `delete-min` operation involves removing the minimum node, making its children new roots, and consolidating the roots by linking the trees of equal degree until at most one tree of each degree remains .
- The `decrease-key` operation involves decreasing the key of a given node, cutting it from its parent if it violates the heap property, and cascading the cuts to its ancestors if they are marked .
- The `delete` operation involves decreasing the key of a given node to negative infinity, and then calling `delete-min`.
- The `merge` operation involves concatenating the root lists of the two heaps, and updating the minimum pointer .

: Fibonacci heap - Wikipedia
: Fibonacci Heap | Brilliant Math & Science Wiki
: Fibonacci Heap | Set 1 (Introduction) - GeeksforGeeks