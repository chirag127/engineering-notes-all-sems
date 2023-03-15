## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., no cycles).
- A **minimum spanning tree (MST)** of a graph is a spanning tree that has the minimum total weight among all the possible spanning trees of the graph.
- **Prim's algorithm** is a greedy algorithm that finds a MST of a given undirected graph with weighted edges.
- The algorithm works as follows:
  - Start with an arbitrary vertex as the root of the MST.
  - Mark the root as visited and add it to the MST.
  - Repeat until all the vertices are visited:
    - Find the minimum weight edge that connects a visited vertex to an unvisited vertex.
    - Mark the unvisited vertex as visited and add the edge to the MST.
- The algorithm can be implemented using a priority queue or a heap data structure to store the edges and their weights.
- The time complexity of the algorithm is O(E log V), where E is the number of edges and V is the number of vertices in the graph.
- The algorithm can be illustrated by the following example:

![Prim's algorithm example](https://upload.wikimedia.org/wikipedia/commons/9/9b/PrimAlgDemo.gif)

- The graph has 6 vertices (A, B, C, D, E, F) and 9 edges with weights.
- The algorithm starts with vertex A as the root of the MST.
- The algorithm finds the minimum weight edge that connects A to an unvisited vertex, which is (A, B) with weight 4. It marks B as visited and adds the edge to the MST.
- The algorithm repeats the process and finds the minimum weight edge that connects a visited vertex to an unvisited vertex, which is (B, C) with weight 8. It marks C as visited and adds the edge to the MST.
- The algorithm repeats the process and finds the minimum weight edge that connects a visited vertex to an unvisited vertex, which is (A, D) with weight 5. It marks D as visited and adds the edge to the MST.
- The algorithm repeats the process and finds the minimum weight edge that connects a visited vertex to an unvisited vertex, which is (D, F) with weight 6. It marks F as visited and adds the edge to the MST.
- The algorithm repeats the process and finds the minimum weight edge that connects a visited vertex to an unvisited vertex, which is (C, E) with weight 5. It marks E as visited and adds the edge to the MST.
- The algorithm terminates as all the vertices are visited and the MST is complete.
- The MST has a total weight of 4 + 8 + 5 + 6 + 5 = 28, which is the minimum among all the possible spanning trees of the graph.