## Find Minimum Spanning Tree using Kruskal’s Algorithm

Kruskal’s Algorithm is a popular algorithm used to find the minimum spanning tree of a given graph. In this algorithm, we start by sorting all the edges of the graph in non-decreasing order of their weights. We then select the edges one by one in ascending order of their weights, and add them to the spanning tree if they do not form a cycle. The process continues until all the vertices of the graph are included in the spanning tree.

### Steps to find Minimum Spanning Tree using Kruskal’s Algorithm:

1. Sort all the edges of the graph in non-decreasing order of their weights.
2. Create a disjoint set for each vertex of the graph.
3. Initialize the minimum spanning tree to an empty set.
4. Iterate through all the edges of the graph in ascending order of their weights:
   - If the two vertices of the edge do not belong to the same disjoint set, add the edge to the minimum spanning tree and merge the two disjoint sets.
   - If the two vertices of the edge already belong to the same disjoint set, discard the edge.
5. Return the minimum spanning tree.

### Advantages of Kruskal’s Algorithm:

- It is easy to understand and implement.
- It is a greedy algorithm, meaning it always selects the edge with the smallest weight at each step, resulting in an optimal solution.
- It can handle disconnected graphs and graphs with cycles.

### Disadvantages of Kruskal’s Algorithm:

- It may not be efficient for large graphs as it requires sorting all the edges of the graph.
- It may not work well for dense graphs as the number of edges to be processed is very large.

### Example:

Consider the following graph:

```
         4
    (1)------(2)
     | \      |
   2 |   \ 5  | 3
     |      \ |
    (4)------(3)
         1
```

The edges of the graph with their weights are:

```
(1,2) -> 4
(1,4) -> 2
(2,3) -> 3
(2,4) -> 5
(3,4) -> 1
```

To find the minimum spanning tree using Kruskal’s Algorithm, we first sort the edges in non-decreasing order of their weights:

```
(1,4) -> 2
(3,4) -> 1
(1,2) -> 4
(2,3) -> 3
(2,4) -> 5
```

We then iterate through the edges in ascending order of their weights, and add them to the minimum spanning tree if they do not form a cycle. The minimum spanning tree for the above graph is:

```
         4
    (1)------(2)
     |        |
   2 |        | 3
     |        |
    (4)------(3)
         1
```

### Applications of Kruskal’s Algorithm:

- It is used in network design and planning.
- It is used in circuit design and routing.
- It is used in computer networking for finding the shortest path between two nodes.