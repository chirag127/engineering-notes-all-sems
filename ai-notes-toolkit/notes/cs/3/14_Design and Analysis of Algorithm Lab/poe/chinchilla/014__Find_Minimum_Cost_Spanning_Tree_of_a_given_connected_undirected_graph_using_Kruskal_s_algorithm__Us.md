## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

In this topic, we will discuss how to find the minimum cost spanning tree of a given connected undirected graph using Kruskal's algorithm and Union-Find algorithms.

### Kruskal's Algorithm

Kruskal's algorithm is a greedy algorithm used to find the minimum cost spanning tree of a connected undirected graph. The algorithm works by sorting the edges of the graph in non-decreasing order of their weights and then adding them to the spanning tree one by one, as long as they do not form a cycle.

The steps involved in Kruskal's algorithm are as follows:

1. Sort the edges of the graph in non-decreasing order of their weights.
2. Initialize an empty set to represent the minimum cost spanning tree.
3. For each edge in the sorted list of edges, add it to the spanning tree if it does not form a cycle with the edges already in the tree.
4. Stop when all the vertices of the graph are included in the spanning tree.

### Union-Find Algorithms

Union-Find algorithms are used to maintain a collection of disjoint sets. They support two operations: union and find. The union operation merges two sets, and the find operation determines the set containing a given element.

The two most common Union-Find algorithms are:

1. Union-by-rank: In this algorithm, the smaller tree is always attached to the root of the larger tree to keep the height of the tree as small as possible. The rank of a tree is the height of its root node.
2. Path compression: In this algorithm, the find operation is optimized by flattening the tree so that all nodes in the path from the root to the given element point directly to the root.

### Kruskal's Algorithm with Union-Find Algorithms

To implement Kruskal's algorithm using Union-Find algorithms, we can use the following steps:

1. Create a disjoint set for each vertex of the graph.
2. Sort the edges of the graph in non-decreasing order of their weights.
3. For each edge in the sorted list of edges, find the sets containing the two vertices of the edge using the find operation.
4. If the sets are not the same, merge them using the union operation and add the edge to the minimum cost spanning tree.
5. Stop when all the vertices of the graph are included in the spanning tree.

### Complexity Analysis

The time complexity of Kruskal's algorithm with Union-Find algorithms is O(E log E), where E is the number of edges in the graph. The space complexity is O(V), where V is the number of vertices in the graph.

### Conclusion

In this topic, we have discussed how to find the minimum cost spanning tree of a given connected undirected graph using Kruskal's algorithm and Union-Find algorithms. By implementing these algorithms, we can efficiently find the minimum cost spanning tree of large graphs, which can be useful in various applications.