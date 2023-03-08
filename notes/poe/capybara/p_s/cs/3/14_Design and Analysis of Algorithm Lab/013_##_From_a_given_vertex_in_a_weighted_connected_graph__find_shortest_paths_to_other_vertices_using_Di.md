## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

Kruskal's algorithm is a greedy algorithm used to find the minimum spanning tree of a given connected undirected graph. The algorithm works by selecting the edges of the graph in increasing order of their weights and adding them to the minimum spanning tree if they do not form a cycle. 

Union-Find is a data structure used to keep track of a partition of a set into disjoint subsets. It is used in Kruskal's algorithm to check if adding an edge to the minimum spanning tree will create a cycle or not. 

The steps involved in finding the minimum spanning tree using Kruskal's algorithm are as follows:

1. Sort the edges of the graph in non-decreasing order of their weights.
2. Initialize a Union-Find data structure with each vertex as a separate set.
3. Iterate through the edges in the sorted order and for each edge, check if adding it to the minimum spanning tree will create a cycle. If not, add it to the minimum spanning tree and merge the sets of the two vertices connected by the edge in the Union-Find data structure.
4. Continue until all edges have been considered or the minimum spanning tree has n-1 edges, where n is the number of vertices in the graph.

Advantages of Kruskal's algorithm:
- Finds the minimum spanning tree of a graph.
- Works well with disconnected graphs.
- Can handle graphs with weighted edges.

Disadvantages of Kruskal's algorithm:
- Can be slow for large graphs.
- Requires sorting of edges, which can be time-consuming.

Example:

Consider the following graph:

```
     2
  A-----B
  |\   /|\
  | \ / | \
  |  X  |  1
  | / \ | /
  |/   \|/
  C-----D
     3
```

The edges and their weights are:

```
AB: 2
AC: 3
AD: 1
BC: 2
BD: 3
CD: 3
```

The minimum spanning tree of the graph using Kruskal's algorithm is:

```
     2
  A-----B
       |
       | 
       |  1
       |
       D
```

Applications of Kruskal's algorithm:
- Network design and planning.
- Circuit design.
- Image segmentation.