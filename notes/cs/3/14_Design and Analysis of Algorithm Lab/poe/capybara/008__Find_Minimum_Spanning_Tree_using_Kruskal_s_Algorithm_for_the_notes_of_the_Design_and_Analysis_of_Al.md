## Find Minimum Spanning Tree using Kruskal’s Algorithm

Kruskal’s Algorithm is a popular algorithm used to find the minimum spanning tree of a connected, weighted graph. The minimum spanning tree is a tree that connects all the vertices of the graph with the minimum total edge weight. In this lab, we will learn how to use Kruskal’s algorithm to find the minimum spanning tree of a graph.

### Overview of Kruskal’s Algorithm

Kruskal’s algorithm is a greedy algorithm that works by selecting the edge with the smallest weight and adding it to the minimum spanning tree. The algorithm then repeats this process until all the vertices are connected. The steps involved in Kruskal’s algorithm are as follows:

1. Initialize the minimum spanning tree to an empty set.
2. Sort all the edges in the graph in ascending order based on their weights.
3. Iterate over all the edges in the sorted order. For each edge, check if adding it to the minimum spanning tree creates a cycle. If not, add the edge to the minimum spanning tree.
4. Repeat step 3 until all the vertices are connected.

### Pseudo code for Kruskal’s Algorithm

```
function KruskalMST(Graph G):
    T = {} // initialize the minimum spanning tree to an empty set
    Sort all the edges in G in ascending order based on their weights
    for each edge (u, v) in G:
        if adding edge (u, v) to T does not create a cycle:
            add edge (u, v) to T
        if |T| == |V| - 1: // |T| is the number of edges in T, |V| is the number of vertices in G
            return T
```

### Example

Let’s consider the following graph:

![Graph](graph.png)

Applying Kruskal’s algorithm to this graph, we get the following minimum spanning tree:

![Minimum Spanning Tree](mst.png)

The total weight of the minimum spanning tree is 37.

### Conclusion

Kruskal’s algorithm is a simple and efficient algorithm for finding the minimum spanning tree of a graph. It has a time complexity of O(E log E), where E is the number of edges in the graph. In this lab, we learned how to use Kruskal’s algorithm to find the minimum spanning tree of a graph.