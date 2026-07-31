## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

### Overview
- A minimum spanning tree (MST) of a connected, undirected graph is a tree that spans all the vertices of the graph with the minimum possible total edge weight.
- Kruskal's algorithm is a greedy algorithm that finds a minimum spanning tree for a connected weighted undirected graph.
- Union-Find is a data structure that helps in finding the minimum spanning tree in Kruskal's algorithm.

### Kruskal's algorithm
- Sort all the edges in non-decreasing order of their weight.
- Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far.
- If the edge doesn't form a cycle, add it to the spanning tree. Otherwise, discard it.
- Repeat steps 2 and 3 until there are (V-1) edges in the spanning tree, where V is the number of vertices in the graph.

### Union-Find algorithm
- Union-Find is a data structure that helps in finding the minimum spanning tree in Kruskal's algorithm.
- It has two main operations: `find` and `union`.
- `find` operation returns the representative element of the set that an element belongs to.
- `union` operation merges two sets into a single set.

### Pseudo code
```
function kruskal(G):
    T = ∅
    for v ∈ G.V:
        make_set(v)
    edges = G.E
    sort(edges)
    for edge in edges:
        u, v = edge
        if find(u) ≠ find(v):
            T.add(edge)
            union(u, v)
    return T
```

### Time complexity
- The time complexity of Kruskal's algorithm is O(ElogE), where E is the number of edges in the graph.
- The time complexity of Union-Find is O(VlogV), where V is the number of vertices in the graph.
- Therefore, the overall time complexity of the algorithm is O(ElogE + VlogV).

### Conclusion
- Kruskal's algorithm is a simple and efficient algorithm for finding the minimum spanning tree of a connected undirected graph.
- Union-Find is a data structure that helps in implementing Kruskal's algorithm efficiently.
- The time complexity of the algorithm is O(ElogE + VlogV).