## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program. for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Kruskal's algorithm is a greedy algorithm that finds a minimum spanning tree for a connected weighted graph.
- The algorithm operates by sorting all the edges in non-decreasing order of their weight.
- Then, it iterates through the sorted edges and adds the edge to the minimum spanning tree if it doesn't form a cycle with the already included edges.
- To check if an edge forms a cycle with the already included edges, we can use the Union-Find algorithm.
- The Union-Find algorithm is used to keep track of the connected components in the graph.
- It has two main operations: Find and Union.
- The Find operation determines if two vertices are in the same connected component.
- The Union operation merges two connected components into one.
- In Kruskal's algorithm, we use the Find operation to check if an edge forms a cycle with the already included edges.
- If the edge doesn't form a cycle, we use the Union operation to merge the connected components of the two vertices of the edge.
- The algorithm continues until all the vertices are in the same connected component, which means that the minimum spanning tree has been found.
- The time complexity of Kruskal's algorithm is O(ElogE) or O(ElogV), where E is the number of edges and V is the number of vertices in the graph.
- The space complexity of the algorithm is O(E+V), where E is the number of edges and V is the number of vertices in the graph.