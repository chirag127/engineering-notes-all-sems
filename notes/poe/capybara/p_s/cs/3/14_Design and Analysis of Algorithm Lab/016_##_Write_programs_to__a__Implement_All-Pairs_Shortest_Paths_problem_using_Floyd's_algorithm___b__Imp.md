## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm

Prim’s algorithm is a greedy algorithm used to find the minimum cost spanning tree of a given undirected graph. It starts by selecting a node as the root node and adding it to a priority queue. The priority queue contains the nodes that are not yet included in the minimum spanning tree. The algorithm then selects the node with the minimum cost and adds it to the minimum spanning tree. This process is repeated until all the nodes are included in the minimum spanning tree.

### Steps to perform Prim’s algorithm:

1. Initialize a priority queue with the root node and set the cost to 0.
2. While the priority queue is not empty, do the following:
   - Select the node with the minimum cost from the priority queue.
   - Add the selected node to the minimum spanning tree.
   - Update the priority queue by adding the neighboring nodes of the selected node that are not already in the minimum spanning tree.
   - Update the cost of the neighboring nodes if necessary.
3. When all the nodes are included in the minimum spanning tree, the algorithm terminates.

### Example:

Consider the following undirected graph:

```
   A---2---B
   |     / |
   3   1   1
   | /     |
   C---2---D
```

The minimum spanning tree using Prim’s algorithm can be found as follows:

1. Start with node A, which has a cost of 0.
2. Add node A to the minimum spanning tree.
3. Add nodes B and C to the priority queue with costs 2 and 3, respectively.
4. Select node B with a cost of 2 and add it to the minimum spanning tree.
5. Update the priority queue by adding node D with a cost of 1.
6. Select node D with a cost of 1 and add it to the minimum spanning tree.
7. Add node C to the priority queue with a cost of 2.
8. Select node C with a cost of 2 and add it to the minimum spanning tree.
9. All nodes are included in the minimum spanning tree, so the algorithm terminates.

The minimum cost spanning tree of the given graph is:

```
   A---2---B
         |
         1
         |
         D---1---C
```

### Advantages of Prim’s algorithm:

- It is easy to understand and implement.
- It is efficient for dense graphs.
- It always finds the minimum cost spanning tree.

### Disadvantages of Prim’s algorithm:

- It is not efficient for sparse graphs.
- It can be slow for large graphs.

### Applications of Prim’s algorithm:

- Network design and optimization.
- Circuit design and optimization.
- Computer networks and communication systems.

In conclusion, Prim’s algorithm is a useful tool for finding the minimum cost spanning tree of a given undirected graph. It is a simple and efficient algorithm that can be applied to various real-world problems.