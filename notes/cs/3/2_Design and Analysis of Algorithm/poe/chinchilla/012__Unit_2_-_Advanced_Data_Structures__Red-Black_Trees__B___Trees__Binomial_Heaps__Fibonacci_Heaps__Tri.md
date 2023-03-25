## Unit 2 - Advanced Data Structures: Red-Black Trees, B – Trees, Binomial Heaps, Fibonacci Heaps, Tries, Skip List

In this unit, we will study some of the advanced data structures that are widely used in computer science. These data structures are designed to provide efficient operations for various problems. Let's take a look at each of them:

### Red-Black Trees

- A red-black tree is a self-balancing binary search tree.
- It ensures that the height of the tree is always O(log n), where n is the number of nodes in the tree.
- It achieves this by adding some constraints and operations to the standard binary search tree.
- The constraints include:
  - Each node is either red or black.
  - The root node is black.
  - Every leaf node is black.
  - If a node is red, then both its children are black.
  - Every path from a node to its descendant leaf nodes contains the same number of black nodes.
- The operations include:
  - Left and right rotations
  - Color flips
- Red-black trees are used in many applications, such as compilers, databases, and set data structures.

### B-Trees

- A B-tree is a self-balancing tree data structure that can store large amounts of data.
- It is commonly used in databases and file systems.
- The B-tree is characterized by:
  - A variable number of keys per node
  - A minimum degree, which specifies the minimum number of keys a node can have
  - Each node can have at most 2d keys, where d is the minimum degree of the tree
  - All leaves appear at the same level
  - Every internal node (except for the root) has at least d children
- B-trees provide efficient operations for searching, inserting, and deleting data.

### Binomial Heaps

- A binomial heap is a collection of binomial trees that satisfy the heap property.
- A binomial tree is a tree that satisfies the following properties:
  - It is a heap
  - It has a unique root node
  - Each node has at most two children
  - The degree of a node is the number of its children
- Binomial heaps are used to implement priority queues.
- They provide efficient operations for inserting, merging, and extracting the minimum element.

### Fibonacci Heaps

- A Fibonacci heap is a collection of heap-ordered trees that satisfy the Fibonacci heap property.
- A heap-ordered tree is a tree in which the parent node has a higher priority than its children.
- The Fibonacci heap property is that each node has a degree at most O(log n), where n is the number of nodes in the heap.
- Fibonacci heaps are used to implement priority queues and graph algorithms.
- They provide efficient operations for inserting, merging, and extracting the minimum element.

### Tries

- A trie is a tree-like data structure that stores a set of strings.
- Each node in the trie represents a prefix of a string.
- The root node represents the empty string.
- Each edge represents a character in a string.
- Tries are used in many applications, such as spell checking, text search, and IP routing.
- They provide efficient operations for searching, inserting, and deleting strings.

### Skip List

- A skip list is a probabilistic data structure that stores a sorted set of elements.
- It consists of a series of linked lists.
- The bottom list contains all the elements in sorted order.
- The higher lists contain a subset of the elements in the lower lists.
- Each element is assigned a random number of levels.
- The skip list provides efficient operations for searching, inserting, and deleting elements.

In conclusion, these advanced data structures provide efficient operations for various problems in computer science. It is important to understand their properties and operations in order to choose the appropriate data structure for a given problem.