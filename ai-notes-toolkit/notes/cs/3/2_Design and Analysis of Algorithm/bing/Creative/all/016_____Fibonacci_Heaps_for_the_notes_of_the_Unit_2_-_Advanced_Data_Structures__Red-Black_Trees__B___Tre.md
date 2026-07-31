# Fibonacci Heaps

- A Fibonacci heap is a data structure for priority queue operations, consisting of a collection of heap-ordered trees  .
- A Fibonacci heap is a collection of trees satisfying the **minimum-heap property**, that is, the key of a child is always greater than or equal to the key of the parent. This implies that the minimum key is always at the root of one of the trees.
- Compared with binomial heaps, the structure of a Fibonacci heap is more flexible. It allows the trees to have any shape, even allowing trees to be single nodes.
- Fibonacci heaps are named after the Fibonacci numbers, which are used in their running time analysis.
- For the Fibonacci heap, the **find-minimum** operation takes constant (**O(1)**) amortized time. The **insert** and **decrease key** operations also work in constant amortized time  .
- The **delete** and **extract-minimum** operations take **O(log n)** amortized time, where **n** is the size of the heap  .
- Fibonacci heaps are used to implement the priority queue element in **Dijkstra’s algorithm** and **Prim's algorithm**, giving the algorithms a very efficient running time .
- Fibonacci heaps are also useful for applications that require frequent updates of key values, such as **network optimization** and **graph algorithms**.

: Fibonacci heap - Wikipedia
: Fibonacci Heap | Brilliant Math & Science Wiki
: Fibonacci Heap | Set 1 (Introduction) - GeeksforGeeks