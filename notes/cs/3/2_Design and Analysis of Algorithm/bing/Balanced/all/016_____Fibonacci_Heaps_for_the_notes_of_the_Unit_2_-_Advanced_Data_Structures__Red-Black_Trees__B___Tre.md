# Fibonacci Heaps

- A Fibonacci heap is a data structure for priority queue operations, consisting of a collection of heap-ordered trees.
- A Fibonacci heap is a collection of trees satisfying the minimum-heap property, that is, the key of a child is always greater than or equal to the key of the parent. This implies that the minimum key is always at the root of one of the trees.
- Fibonacci heaps are named after the Fibonacci numbers, which are used in their running time analysis.
- Fibonacci heaps are used to implement the priority queue element in Dijkstra’s algorithm, giving the algorithm a very efficient running time.
- The key advantage of a Fibonacci heap over other heap data structures is its fast amortized running time for operations such as insert, find-minimum, and decrease-key.
- The insert and find-minimum operations work in constant (O(1)) amortized time. The decrease-key operation also works in constant amortized time.
- The delete and delete-minimum operations work in O(log n) amortized time, where n is the number of nodes in the heap.
- The merge operation, which combines two Fibonacci heaps into one, works in constant (O(1)) actual time.
- The structure of a Fibonacci heap is more flexible than a binary heap or a binomial heap, as it allows arbitrary degrees of nodes and does not enforce a strict shape of the trees.
- A Fibonacci heap maintains a pointer to the minimum node and a list of roots of the trees. Each node stores its key, degree, parent, child, left sibling, and right sibling pointers.
- A Fibonacci heap also maintains a potential function, which is a measure of how unbalanced the heap is. The potential function is used to analyze the amortized running time of the operations.
- A Fibonacci heap uses two techniques to improve the efficiency of its operations: lazy insertion and cascading cuts. Lazy insertion means that new nodes are simply added to the root list without any restructuring. Cascading cuts means that when a node loses a child due to a decrease-key operation, it may also be cut from its parent and added to the root list, and this process may continue recursively.
- A Fibonacci heap performs a consolidation operation when a delete or delete-minimum operation is performed. Consolidation reduces the number of trees in the heap by merging trees of equal degree until there is at most one tree of each degree.
- A Fibonacci heap can be represented by a circular, doubly linked list of roots, and each root can be the head of a circular, doubly linked list of children. The following diagram shows an example of a Fibonacci heap with 15 nodes and 5 trees:

![Fibonacci heap example](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Fibonacci_heap.svg/1200px-Fibonacci_heap.svg.png)

: Fibonacci heap - Wikipedia
: Fibonacci Heap | Brilliant Math & Science Wiki
: Fibonacci Heap | Set 1 (Introduction) - GeeksforGeeks