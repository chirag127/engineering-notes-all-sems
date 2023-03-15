Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of finding minimum spanning tree using Kruskal's algorithm for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System.

## Find Minimum Spanning Tree using Kruskal’s Algorithm

- A **minimum spanning tree** (MST) is a subset of the edges of a connected, edge-weighted graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST for a graph by adding edges in increasing order of weight, as long as they do not create a cycle.
- The steps of Kruskal's algorithm are :
  - Sort all the edges in non-decreasing order of their weight.
  - Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
  - Repeat step 2 until there are (V-1) edges in the spanning tree, where V is the number of vertices in the graph.
- To check if an edge forms a cycle with the spanning tree, we can use a **union-find** data structure that keeps track of the connected components of the graph.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices, since the most time-consuming operation is sorting the edges.
- The space complexity of Kruskal's algorithm is O(E + V), since we need to store the edges and the union-find data structure.
- An example of applying Kruskal's algorithm to a graph is shown below:

![Kruskal's algorithm example](https://media.geeksforgeeks.org/wp-content/uploads/kruskals-algorithm.png)