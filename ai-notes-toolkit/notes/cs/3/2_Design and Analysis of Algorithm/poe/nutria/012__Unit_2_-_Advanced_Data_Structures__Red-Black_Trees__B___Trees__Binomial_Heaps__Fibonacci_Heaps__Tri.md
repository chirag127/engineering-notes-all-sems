
## Unit 2 - Advanced Data Structures: Red-Black Trees, B – Trees, Binomial Heaps, Fibonacci Heaps, Tries, Skip List

1. Red-Black Trees: Red-Black Trees are a type of self-balancing binary search tree. They are used to store and organize data in a way that is both efficient and easy to search. Red-Black Trees have a number of properties that make them ideal for use in data storage and retrieval. These properties include:

- Every node is either red or black.
- The root is black.
- Every leaf (NIL) is black.
- If a node is red, then both its children are black.
- Every path from a given node to any of its descendant NIL nodes contains the same number of black nodes.

2. B-Trees: B-Trees are a type of self-balancing multi-way search tree. They are used to store and organize data in a way that is both efficient and easy to search. B-Trees have a number of properties that make them ideal for use in data storage and retrieval. These properties include:

- Every node has at least two children.
- Every node has a number of keys equal to the number of children.
- All keys are sorted in order.
- The root node can have any number of keys.
- All non-root nodes must have between (M/2) and M keys.

3. Binomial Heaps: Binomial Heaps are a type of self-balancing binary heap. They are used to store and organize data in a way that is both efficient and easy to search. Binomial Heaps have a number of properties that make them ideal for use in data storage and retrieval. These properties include:

- Every node has two children.
- Every node has a degree equal to the number of children.
- All nodes in the same level must have the same degree.
- The root node can have any degree.
- All non-root nodes must have a degree between 0 and (log2N).

4. Fibonacci Heaps: Fibonacci Heaps are a type of self-balancing binary heap. They are used to store and organize data in a way that is both efficient and easy to search. Fibonacci Heaps have a number of properties that make them ideal for use in data storage and retrieval. These properties include:

- Every node has two children.
- Every node has a degree equal to the number of children.
- All nodes in the same level must have the same degree.
- The root node can have any degree.
- All non-root nodes must have a degree between 0 and (log2N).
- Every node has a degree at least equal to its parent's degree.

5. Tries: Tries are a type of self-balancing tree. They are used to store and organize data in a way that is both efficient and easy to search. Tries have a number of properties that make them ideal for use in data storage and retrieval. These properties include:

- Every node has an array of children.
- Every node has a number of children equal to the number of characters in the alphabet.
- All nodes are sorted in alphabetical order.
- The root node has no children.
- All non-root nodes must have between 0 and (N-1) children.

6. Skip List: Skip Lists are a type of self-balancing linked list. They are used to store and organize data in a way that is both efficient and easy to search. Skip Lists have a number of properties that make them ideal for use in data storage and retrieval. These properties include:

- Every node has two or more pointers.
- Every node has a level equal to the number of pointers.
- All nodes in the same level must have the same number of pointers.
- The root node can have any level.
- All non-root nodes must have a level between 0 and (log2N).
- Every node has a level at least equal to its parent's level.