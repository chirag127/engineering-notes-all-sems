### Fibonacci Heaps

- A Fibonacci heap is a data structure for priority queue operations, consisting of a collection of heap-ordered trees.
- A Fibonacci heap is a collection of trees satisfying the minimum-heap property, that is, the key of a child is always greater than or equal to the key of the parent. This implies that the minimum key is always at the root of one of the trees.
- A Fibonacci heap is a specific implementation of the heap data structure that makes use of Fibonacci numbers. Fibonacci heaps are used to implement the priority queue element in Dijkstra’s algorithm, giving the algorithm a very efficient running time.
- Fibonacci heaps are named after the Fibonacci numbers, which are used in their running time analysis. For the Fibonacci heap, the find-minimum operation takes constant (O(1)) amortized time. The insert and decrease key operations also work in constant amortized time. The delete and delete-minimum operations work in O(log n) amortized time, where n is the size of the heap.
- The structure of a Fibonacci heap is more flexible than a binary heap or a binomial heap. A Fibonacci heap does not have a fixed shape, and it allows the trees to have arbitrary degree. The trees are linked together by a circular doubly linked list, which maintains the roots of the trees. The minimum element of the heap can be easily accessed by a pointer to the minimum root .
- A Fibonacci heap supports the following operations:

  - **make-heap**: creates and returns a new empty Fibonacci heap.
  - **insert**: inserts a new node with a given key into the heap.
  - **find-min**: returns the node with the minimum key in the heap.
  - **union**: merges two Fibonacci heaps into one, and returns the resulting heap.
  - **extract-min**: removes and returns the node with the minimum key from the heap, and rearranges the remaining nodes.
  - **decrease-key**: decreases the key of a given node in the heap, and updates the heap structure if necessary.
  - **delete**: removes a given node from the heap, and updates the heap structure if necessary.

- The main idea behind the Fibonacci heap is to delay the work of consolidating the trees until a delete or extract-min operation is performed. This way, the insert and decrease-key operations can be done quickly, and the amortized cost of the other operations can be reduced. The Fibonacci heap uses two techniques to achieve this: lazy insertion and cascading cut.
- Lazy insertion means that when a new node is inserted into the heap, it is simply added to the root list, without merging it with any existing tree. This allows the insert operation to be done in constant time, but it may increase the number of trees in the heap.
- Cascading cut means that when a node is cut from its parent due to a decrease-key operation, it is marked to indicate that it has lost one child. If a marked node loses another child, it is cut from its parent as well, and the parent is marked. This process continues until either the root is reached, or an unmarked node is found. This allows the decrease-key operation to be done in constant time, but it may increase the potential of the heap, which is a measure of how much work is deferred.
- The potential of a Fibonacci heap is defined as:

  - phi(H) = t(H) + 2m(H)

  where t(H) is the number of trees in the root list of H, and m(H) is the number of marked nodes in H.

- The potential of a Fibonacci heap is used to analyze the amortized running time of the operations. The amortized cost of an operation is defined as:

  - hat{c}(i) = c(i) + phi(H_i) - phi(H_{i-1})

  where c(i) is the actual cost of the i-th operation, and H_i is the state of the heap after the i-th operation.

- The amortized running time of the Fibonacci heap operations are as follows:

  - **make-heap**: O(1) (actual and amortized)
  - **insert**: O(1) (actual and amortized)
  - **find-min**: O(1) (actual and amortized)
  - **union**: O(1) (actual and amortized)
  - **extract-min**: O(log n) (amortized)
  - **decrease-key**: O(